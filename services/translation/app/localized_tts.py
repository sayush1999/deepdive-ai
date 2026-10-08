from google.cloud import texttospeech

# Language codes the UI offers; extend as needed
LANG_TO_TTS = {"en": "en-IN", "hi": "hi-IN", "bn": "bn-IN", "ta": "ta-IN"}

def synthesize(text: str, lang: str = "en") -> bytes:
    """Return MP3 bytes narrating `text` in the given language."""
    client = texttospeech.TextToSpeechClient()
    resp = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=text),
        voice=texttospeech.VoiceSelectionParams(language_code=LANG_TO_TTS.get(lang, "en-IN")),
        audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3),
    )
    return resp.audio_content
