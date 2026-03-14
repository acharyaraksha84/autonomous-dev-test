import requests
from config import GITHUB_TOKEN, OWNER, REPO

def get_issues():

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    issues = response.json()

    return issues