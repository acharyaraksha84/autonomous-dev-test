from pr_creator import create_pull_request

title = "AI Fix: Login validation bug"

body = """
AI generated fix for login validation bug.

The issue allowed empty passwords.

AI suggested adding password validation.
"""

response = create_pull_request(title, body)

print(response)