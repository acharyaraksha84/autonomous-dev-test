from issue_reader import get_issues

issues = get_issues()

for issue in issues:
    print("Issue Title:", issue["title"])
    print("Issue Body:", issue["body"])
    print("-------------")