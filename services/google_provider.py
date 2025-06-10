import requests

def translate_with_google(text, source, target, api_key, context="General"):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "source": source[:2].lower(),
        "target": target[:2].lower(),
        "format": "text",
        "key": api_key
    }

    response = requests.post(url, params=params)
    result = response.json()

    if "error" in result:
        raise RuntimeError(result["error"]["message"])

    return result["data"]["translations"][0]["translatedText"]
