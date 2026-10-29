#!/usr/bin/env python3
"""Prepare unique audio tracks and optional transcripts from a local video folder.

Requires ffmpeg; transcription additionally requires faster-whisper in the active
Python environment. No dependencies are installed by this script.
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


VIDEO_EXTENSIONS = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi"}


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def prepare(folder, output, transcriber=None):
    """Return a manifest; track failures explicitly and preserve same-stem files."""
    files = sorted(p for p in folder.iterdir()
                   if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS)
    if not files:
        raise ValueError("No supported videos found in the input folder")
    audio_dir = output / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    tracks = {}
    entries = []
    for source in files:
        # Including the full filename prevents foo.mp4 / foo.mov collisions.
        source_key = hashlib.sha256(source.name.encode("utf-8")).hexdigest()[:16]
        audio = audio_dir / (source_key + ".pcm")
        entry = {"source": str(source.resolve()), "filename": source.name}
        try:
            subprocess.run([
                "ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(source),
                "-vn", "-ac", "1", "-ar", "16000", "-acodec", "pcm_s16le",
                "-f", "s16le", str(audio),
            ], check=True, capture_output=True)
            if audio.stat().st_size == 0:
                raise ValueError("Extracted audio is empty")
            digest = sha256_file(audio)
            canonical = audio_dir / (digest + ".wav")
            if digest not in tracks:
                # WAV container is generated from canonical PCM for ASR input.
                subprocess.run([
                    "ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "s16le",
                    "-ar", "16000", "-ac", "1", "-i", str(audio),
                    str(canonical),
                ], check=True, capture_output=True)
                track = {"audio_sha256": digest, "audio": str(canonical.resolve()),
                         "first_source": source.name}
                if transcriber:
                    transcript = output / (digest + ".txt")
                    transcript.write_text(transcriber(canonical), encoding="utf-8")
                    track["transcript"] = str(transcript.resolve())
                tracks[digest] = track
            entry.update(tracks[digest])
            entry["status"] = "transcribed" if transcriber else "extracted"
        except Exception as error:
            detail = str(error)
            if isinstance(error, subprocess.CalledProcessError):
                detail = error.stderr.decode("utf-8", errors="replace")[-2000:]
            entry.update(status="failed", error=detail)
        finally:
            audio.unlink(missing_ok=True)
        entries.append(entry)
    return {"mode": "transcribe" if transcriber else "extract-only",
            "files": entries, "unique_audio_tracks": len(tracks),
            "failures": sum(e["status"] == "failed" for e in entries)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--extract-only", action="store_true")
    parser.add_argument("--model", default="base", help="Local model path or model name")
    parser.add_argument("--language", default="auto", help="Language code or auto")
    parser.add_argument("--beam", type=int, default=1)
    args = parser.parse_args(argv)
    if not args.folder.is_dir():
        parser.error("Input must be an existing folder")
    if not shutil.which("ffmpeg"):
        parser.error("ffmpeg is required and was not found on PATH")
    if args.beam < 1:
        parser.error("--beam must be positive")
    transcriber = None
    if not args.extract_only:
        try:
            from faster_whisper import WhisperModel
        except ImportError:
            parser.error("Transcription needs faster-whisper in this Python environment; use --extract-only for audio preparation")
        model = WhisperModel(args.model, device="cpu", compute_type="int8")

        def transcriber(audio):
            segments, _ = model.transcribe(str(audio), beam_size=args.beam,
                                          language=None if args.language == "auto" else args.language)
            return " ".join(segment.text.strip() for segment in segments).strip()
    try:
        manifest = prepare(args.folder, args.out, transcriber)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2
    manifest_path = args.out / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_path.resolve()),
                      "unique_audio_tracks": manifest["unique_audio_tracks"],
                      "failures": manifest["failures"]}, indent=2))
    return 1 if manifest["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
