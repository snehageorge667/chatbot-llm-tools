import requests
import json

OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "phi3:mini"

async def get_llm_response(prompt: str, history: list):
    # Combine chat history into single context string
    context = "\n".join([f"{m['role']}: {m['content']}" for m in history])
    full_prompt = f"{context}\nUser: {prompt}\nAssistant:"

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from LLM.")
    except Exception as e:
        return f"Error: {str(e)}"
