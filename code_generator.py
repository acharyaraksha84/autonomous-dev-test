import requests
from config import OLLAMA_URL, MODEL

def generate_code(issue_text):

    prompt = f"""
You are an AI software developer.

A GitHub issue describes a bug.

Issue:
{issue_text}

Suggest a Python code fix for this issue.
Return only the corrected code.
"""

    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=data)

    return response.json()["response"]