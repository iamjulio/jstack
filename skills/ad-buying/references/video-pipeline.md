# Video batch to paused ads

1. Inventory authorized source files with stable IDs or paths, filenames, sizes, duration, language and intended offer. Use the storage connector's supported binary download or accessible local files; do not put large base64 media into model context.
2. Extract a consistent mono audio track and hash it to identify exact audio duplicates. Identical audio can reuse a transcript; it does not prove the visuals, captions, embedded CTA or destination are identical. Visually inspect variants before sharing copy or collapsing a creative test.
3. Transcribe each unique audio track with available local or approved hosted tooling. The optional [transcription helper](../scripts/transcribe_videos.py) uses FFmpeg and faster-whisper. Run `--help` first. Model downloads need network and local space; do not promise a fixed runtime or install dependencies into a user's global environment.
4. Preserve raw text and uncertain terms, especially product names, numbers, dates and prices. Inspect the video for on-screen claims absent from audio. Write grounded copy using [copy and evidence](copy-and-evidence.md).
5. Upload through the supported connector or authorized native UI; if neither is available, produce the upload manifest and remaining step. Match platform IDs back to the exact asset, not only a possibly duplicated filename. Verify processing and thumbnails.
6. Build one representative paused ad with verified identity, destination/UTMs, CTA, thumbnail and text. Read back and preview it before the remaining authorized batch. Match every copy block to its asset and resulting platform ID.
7. Reconcile expected versus actual count and statuses. Review placement previews, including changed CTA cuts. Report preview links, parent/child status and any unresolved uploads or review failures. Launch is a separate authorized action governed by the main skill.

Example local preparation:

```bash
python3 scripts/transcribe_videos.py /path/to/videos --out /path/to/transcripts --extract-only
python3 scripts/transcribe_videos.py /path/to/videos --out /path/to/transcripts --language auto
```

Run these from the skill folder, or use the helper's absolute path. `--extract-only` inventories/deduplicates audio without loading a speech model. The helper writes a manifest and exits nonzero on partial failures so missing files cannot silently look like a complete batch.
