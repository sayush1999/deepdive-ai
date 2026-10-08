import os
from google.cloud import translate_v3 as translate

_client = None

def translate_text(texts: list[str], target_lang: str, source_lang: str = "en") -> list[str]:
    """Translate a batch of strings with Cloud Translation (v3)."""
    global _client
    if _client is None:
        _client = translate.TranslationServiceClient()
    parent = f"projects/{os.environ['GCP_PROJECT_ID']}/locations/global"
    resp = _client.translate_text(
        contents=texts,
        target_language_code=target_lang,
        source_language_code=source_lang,
        parent=parent,
        mime_type="text/plain",
    )
    return [t.translated_text for t in resp.translations]
