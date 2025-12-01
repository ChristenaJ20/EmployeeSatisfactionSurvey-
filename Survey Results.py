# Chelsi Bookal

import csv
from collections import Counter

def load_survey_results(filename="survey_results.csv"):
    # Loading survey results from CSV file.
    submissions = []
    with open(filename,"r") as f:
        reader = csv.DictReader(f)
        # Converting each row into a dictionary with proper types.
        for row in reader:
            row["rating"] = int(row["rating"])
            submissions.append(row)
    return submissions

def show_results(submissions):
    # Checking if there are submissions to display.
    if not submissions:
        print("No survey submissions found.")
        return

    # Calculating the average rating.
    ratings = [s["rating"] for s in submissions]
    avg = sum(ratings)/len(ratings)
    print(f"Average Rating: {avg:.2f}")

    # Finding the most common comment.
    comments = [s["comment"] for s in submissions]
    most_common = Counter(comments).most_common(1)[0][0]
    print(f"Most Common Comment: {most_common}")

    # Grouping and displaying submissions by department.
    departments = {}
    for s in submissions:
        dept = s["department"]
        departments.setdefault(dept, []).append(s)
    print("\nSubmissions by Department:")
    for dept, items in departments.items():
        print(f"\n{dept}:")
        for item in items:
            # Displaying username or "Anonymous".
            name = "Anonymous" if item["anonymous"] else item["username"]
            print(f"- {name}: Rating {item['rating']}, Comment: {item['comment']}")

if __name__ == "__main__":
    # Loading survey results and displaying for stakeholders.
    subs = load_survey_results()
    show_results(subs)
