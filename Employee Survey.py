# Chelsi Bookal 

import csv
class SurveyManager:
    """Managing survey submissions and validations."""

    def __init__(self):
        # Initializing list to store survey submissions.
        self.submissions = []

    def validate_submission(self, department, rating, comment):
        # Checking that department is provided.
        if not department:
            raise ValueError("Department is required.")
        # Checking that rating is provided.
        if rating is None:
            raise ValueError("Rating is required.")
        # Checking that comment is provided.
        if not comment:
            raise ValueError("Comment is required.")

    def submit_survey(self, department, rating, comment, anonymous=False, username=None):
        # Validating submission before storing.
        self.validate_submission(department, rating, comment)
        # Setting username to None if anonymous.
        user = None if anonymous else username
        # Storing the survey entry in submissions.
        entry = {
            "department": department,
            "rating": rating,
            "comment": comment,
            "anonymous": anonymous,
            "username": user
        }
        self.submissions.append(entry)

    def save_to_file(self, filename="survey_results.csv"):
        # Sorting submissions by department before saving.
        sorted_list = sorted(self.submissions, key=lambda x: x["department"])
        # Writing survey submissions to CSV file.
        with open(filename, "w", newline="") as f:
            fieldnames = ["department","rating","comment","anonymous","username"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            # Writing each submission to file.
            for row in sorted_list:
                writer.writerow(row)

def run_employee_survey():
    # Starting the employee survey interaction.
    sm = SurveyManager()
    print("Welcome to the Employee Survey!")

    while True:
        # Asking for employee name.
        username = input("Enter your name (leave blank if anonymous): ").strip()
        # Asking for employee department.
        department = input("Department: ").strip()
        while not department:
            print("Department is required.")
            department = input("Department: ").strip()

        # Asking for employee rating.
        try:
            rating = int(input("Rating (1-5): ").strip())
            while rating < 1 or rating > 5:
                print("Rating must be 1-5.")
                rating = int(input("Rating (1-5): ").strip())
        except:
            print("Invalid rating. Enter a number 1-5.")
            continue

        # Asking for employee comment.
        comment = input("Comment: ").strip()
        while not comment:
            print("Comment is required.")
            comment = input("Comment: ").strip()

        # Asking if employee wants to submit anonymously.
        anonymous_input = input("Submit anonymously? (y/n): ").strip().lower()
        anonymous = anonymous_input == 'y' or username==''

        # Submitting the survey.
        sm.submit_survey(department, rating, comment, anonymous, username if not anonymous else None)
        print("Thank you! Survey submitted.\n")

        # Checking if another employee wants to take the survey.
        cont = input("Next employee? (y/n): ").strip().lower()
        if cont != 'y':
            break

    # Saving all survey submissions to file.
    sm.save_to_file()
    print("All survey responses saved to survey_results.csv.")

if __name__ == "__main__":
    # Running the employee survey.
    run_employee_survey()
