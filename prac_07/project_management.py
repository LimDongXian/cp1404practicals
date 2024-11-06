"""
Project Management
Estimate: 2 Hours
Actual:   3 Hours
"""
import datetime
from prac_07.project import Project

MENU = (" - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by date\n"
        " - (A)dd new project\n - (U)pdate project\n - (Q)uit")
FILENAME = "projects.txt"
PERCENTAGE_THRESHOLD = 100
PRIORITY_THRESHOLD = 10
MINIMUM_NUMBER = 0


def main():
    projects = load_file(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load projects: ")
            load_file(filename)
        elif choice == "S":
            save_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_project(projects, date_string)
        elif choice == "A":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    is_save = input(f"Would you like to save to {FILENAME}? ").lower()
    if "yes" in is_save:
        save_file(projects)
    print("Thank you for using custom-built project management software.")


def load_file(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            part = line.strip().split("	")
            project = Project(str(part[0]), part[1], int(part[2]), float(part[3]), int(part[4]))
            projects.append(project)
        return projects


def save_file(projects):
    """Save the list of projects to the default FILENAME file."""
    with open(FILENAME, 'w') as out_file:
        out_file.write("\n")  # To prevent first line data lost as load file skip header
        for project in projects:
            out_file.write(f"{project.name}	{project.start_date.strftime("%d/%m/%Y")}	{project.priority}"
                           f"	{project.cost_estimate}	{project.completion_percentage}\n")
    print("Project Saved")


def display_projects(projects):
    """Display projects, separating incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]
    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)
    print("Completed projects:")
    for project in sorted(completed_projects):
        print(project)


def filter_project(projects, date):
    """Filter projects to show only those that start after a specified date."""
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = sorted((project for project in projects if project.start_date >= date),
                               key=lambda project: project.start_date)
    for project in filtered_projects:
        print(project)


def add_project(projects):
    """Add a new project with details and add it to the project list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    """Update an existing project's priority and completion percentage."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = get_valid_number("Project choice: ", len(projects) - 1, MINIMUM_NUMBER)
    selected_project = projects[project_choice]
    print(selected_project)
    new_percentage = get_valid_number("New percentage: ", PERCENTAGE_THRESHOLD, MINIMUM_NUMBER)
    new_priority = get_valid_number("New priority: ", PRIORITY_THRESHOLD, MINIMUM_NUMBER)
    selected_project.update_project(new_priority, new_percentage)


def get_valid_number(prompt, high, low):
    """Prompt the user to enter a number within a valid range (low to high)"""
    """Return empty string if user enters invalid.(for priority and completion percentage"""
    try:
        number = int(input(prompt))
        while number < low or number > high:
            print("Invalid number")
            number = int(input(prompt))
    except ValueError:
        return ""
    return number


main()
