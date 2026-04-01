from pathlib import Path


def transcribe_audio(audio_file_path: str) -> dict:
    """
    Minimal Whisper wrapper for local transcription.
    Falls back to a friendly error payload if Whisper is unavailable.
    """
    path = Path(audio_file_path)
    if not path.exists():
        return {"ok": False, "error": "Audio file not found", "text": ""}

    try:
        import whisper

        model = whisper.load_model("small")
        result = model.transcribe(str(path))
        return {"ok": True, "error": None, "text": result.get("text", "").strip()}
    except Exception as exc:
        return {
            "ok": False,
            "error": f"Whisper unavailable: {exc}",
            "text": "",
        }
