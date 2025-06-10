import json
import re
from langdetect import detect

def load_synonym_data(language_code):
    """Load context-based synonym dictionary based on detected language."""
    if language_code == "fr":
        path = "config/synonyms_fr.json"
    elif language_code == "en":
        path = "config/synonyms_en.json"
    else:
        return {}

    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def suggest_synonyms(text, context):
    """Apply synonyms to translated text based on detected language and selected context."""
    try:
        lang = detect(text)
    except Exception:
        lang = "en"

    synonym_data = load_synonym_data(lang)

    if context not in synonym_data:
        return text

    for base_word, synonyms in synonym_data[context].items():
        # Word boundary regex to avoid partial matches (e.g., "student" inside "studentship")
        pattern = r'\b' + re.escape(base_word) + r'\b'
        replacement = f"{base_word} ({'/'.join(synonyms)})"
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    return text
