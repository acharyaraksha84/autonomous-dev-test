import os

def find_relevant_file(issue_text):

    keywords = issue_text.lower().split()

    project_path = "."

    best_file = None
    best_score = 0

    for root, dirs, files in os.walk(project_path):

        for file in files:

            if not file.endswith(".py"):
                continue

            # skip system / test files
            if file.startswith("test") or file in ["main.py","pr_creator.py","issue_reader.py","reviewer.py","code_generator.py"]:
                continue

            path = os.path.join(root, file)

            score = 0

            # file name scoring (VERY important)
            filename = file.lower()

            for word in keywords:
                if word in filename:
                    score += 5

            try:

                with open(path, "r", encoding="utf-8") as f:

                    content = f.read().lower()

                    for word in keywords:
                        if word in content:
                            score += 1

            except:
                pass

            if score > best_score:
                best_score = score
                best_file = path

    return best_file