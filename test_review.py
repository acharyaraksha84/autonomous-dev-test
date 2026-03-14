from issue_reader import get_issues
from code_generator import generate_code
from reviewer import review_code

issues = get_issues()

issue = issues[0]

issue_text = issue["title"] + "\n" + issue["body"]

print("ISSUE:")
print(issue_text)

print("\nGENERATED CODE:\n")

code = generate_code(issue_text)

print(code)

print("\nAI REVIEW:\n")

review = review_code(code)

print(review)