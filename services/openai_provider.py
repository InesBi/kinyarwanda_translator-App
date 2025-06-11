from openai import OpenAI

def translate_with_openai(text, source, target, api_key, context="General"):
    client = OpenAI(api_key=api_key)
    
    system_prompt = (
        f"You are a professional translator specializing in the {context.lower()} domain. "
        f"Translate the following text from {source} to {target}, using accurate and formal language appropriate to the {context.lower()} context."
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3
    )
    
    return response.choices[0].message.content.strip()
