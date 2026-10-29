"""Local preparation tests; no model, network, or ad account is used."""

import importlib.util
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "transcribe_videos", Path(__file__).with_name("transcribe_videos.py"))
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg is required")
class PreparationTests(unittest.TestCase):
    def tone(self, path, frequency):
        subprocess.run([
            "ffmpeg", "-nostdin", "-v", "error", "-f", "lavfi", "-i",
            f"sine=frequency={frequency}:sample_rate=16000", "-t", "0.1",
            "-c:a", "pcm_s16le", str(path),
        ], check=True, capture_output=True)

    def test_exact_dedupe_same_stem_and_partial_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inputs = root / "inputs"
            inputs.mkdir()
            self.tone(inputs / "same.mkv", 440)
            self.tone(inputs / "same.mov", 880)
            shutil.copyfile(inputs / "same.mkv", inputs / "duplicate.mkv")
            (inputs / "broken.mp4").write_bytes(b"invalid media")
            calls = []

            def transcribe(audio):
                calls.append(audio)
                return f"Transcript for {audio.stem}"

            result = MODULE.prepare(inputs, root / "output", transcribe)
            self.assertEqual(result["failures"], 1)
            self.assertEqual(result["unique_audio_tracks"], 2)
            self.assertEqual(len(calls), 2)
            files = {entry["filename"]: entry for entry in result["files"]}
            self.assertEqual(files["same.mkv"]["transcript"],
                             files["duplicate.mkv"]["transcript"])
            self.assertNotEqual(files["same.mkv"]["transcript"],
                                files["same.mov"]["transcript"])
            self.assertEqual(files["broken.mp4"]["status"], "failed")

    def test_transcription_failure_is_recorded(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            inputs = root / "inputs"
            inputs.mkdir()
            self.tone(inputs / "clip.mkv", 440)

            def fail(_audio):
                raise RuntimeError("ASR unavailable")

            result = MODULE.prepare(inputs, root / "output", fail)
            self.assertEqual(result["failures"], 1)
            self.assertEqual(result["files"][0]["error"], "ASR unavailable")


if __name__ == "__main__":
    unittest.main()
