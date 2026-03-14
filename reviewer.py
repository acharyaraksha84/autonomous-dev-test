import requests
from config import OLLAMA_URL, MODEL

def review_code(code):

    prompt = f"""
You are a senior software engineer reviewing a pull request.

Review the following Python code and provide feedback.

Check for:
- bugs
- security issues
- improvements
- best practices

Code:
{code}
"""

    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=data)

    return response.json()["response"]