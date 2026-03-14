from issue_reader import get_issues
from code_generator import generate_code
from reviewer import review_code
from pr_creator import create_pull_request, merge_pull_request
from code_search import find_relevant_file


# Step 1: Read issues
issues = get_issues()

issue = issues[0]

issue_title = issue["title"]
issue_body = issue["body"]

issue_text = issue_title + "\n" + issue_body

print("ISSUE:")
print(issue_text)


# Step 2: Find relevant file in repo
target_file = find_relevant_file(issue_text)

print("\nRELEVANT FILE FOUND:")
print(target_file)


# Step 3: Generate code fix
print("\nGENERATED CODE:\n")

code = generate_code(issue_text)

print(code)


# Step 4: Review generated code
print("\nAI REVIEW:\n")

review = review_code(code)

print(review)


# Step 5: Create Pull Request
title = "AI Fix: " + issue_title

body = f"""
AI Generated Fix

Issue:
{issue_text}

Target File:
{target_file}

Generated Code:
{code}

AI Review:
{review}
"""


response = create_pull_request(title, body, target_file)

print("\nPULL REQUEST RESPONSE:\n")
print(response)


# Step 6: Auto merge PR
if "number" in response:

    pr_number = response["number"]

    print("\nPULL REQUEST CREATED:")
    print(response["html_url"])

    merge_response = merge_pull_request(pr_number)

    print("\nAUTO MERGE RESULT:")
    print(merge_response)

else:

    print("\nPR creation failed:")
    print(response)