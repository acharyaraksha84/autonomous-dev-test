import requests
import time
import base64
import os
from config import GITHUB_TOKEN, OWNER, REPO

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


# get latest commit SHA
def get_main_sha():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/ref/heads/main"
    response = requests.get(url, headers=headers)
    return response.json()["object"]["sha"]


# create new branch
def create_branch(branch_name):

    sha = get_main_sha()

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/refs"

    data = {
        "ref": f"refs/heads/{branch_name}",
        "sha": sha
    }

    requests.post(url, headers=headers, json=data)


# commit file change
def commit_file(branch_name, file_path, new_content):

    import os

    # convert windows path
    file_path = os.path.relpath(file_path).replace("\\", "/")

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{file_path}"

    response = requests.get(url, headers=headers)

    file_data = response.json()

    if "sha" not in file_data:
        print("\nERROR: GitHub could not find file:", file_path)
        print(file_data)
        return

    sha = file_data["sha"]

    encoded_content = base64.b64encode(new_content.encode()).decode()

    commit_data = {
        "message": "AI generated fix",
        "content": encoded_content,
        "sha": sha,
        "branch": branch_name
    }

    requests.put(url, headers=headers, json=commit_data)


# create pull request
def create_pull_request(title, body, target_file):

    branch_name = "ai-fix-" + str(int(time.time()))

    create_branch(branch_name)

    # commit AI change to detected file
    commit_file(branch_name, target_file, body)

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls"

    data = {
        "title": title,
        "body": body,
        "head": branch_name,
        "base": "main"
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()


# merge pull request
def merge_pull_request(pr_number):

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/merge"

    data = {
        "commit_title": "Auto merged AI fix",
        "merge_method": "merge"
    }

    response = requests.put(url, headers=headers, json=data)

    return response.json()