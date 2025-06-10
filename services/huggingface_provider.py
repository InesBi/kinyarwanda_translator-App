import requests

def translate_with_huggingface(text, source, target, api_key, context="General"):
    model_id = "your model choice" + source[:2].lower() + "-" + target[:2].lower()
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": text}
    response = requests.post(
        f"https://api-inference.huggingface.co/models/{model_id}",
        headers=headers,
        json=payload
    )
    result = response.json()
    
    if isinstance(result, list):
        return result[0]["translation_text"]
    elif "error" in result:
        raise RuntimeError(result["error"])
    else:
        raise ValueError("Unexpected response from Hugging Face API")
