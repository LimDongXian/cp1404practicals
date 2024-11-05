"""
Project Management
Estimate: 30 minutes
Actual:    minutes
"""
import datetime
from prac_07.project import Project

MENU = (" - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by dat\n"
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
            projects = load_file(filename)
        elif choice == "S":
            print("Save projects")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("Filter projects by date")
        elif choice == "A":
            print("Let's add a new project")
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_file(filename):
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            part = line.strip().split("	")
            project = Project(str(part[0]), part[1], int(part[2]), float(part[3]), int(part[4]))
            projects.append(project)
        return projects


def save_file(projects):
    with open(FILENAME, 'w') as out_file:
        for project in projects:
            out_file.write(f"{project.name}, {project.start_data}, {project.priority}"
                           f", {project.cost_estimate}, {project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]
    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)
    print("Completed projects:")
    for project in sorted(completed_projects):
        print(project)


def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = get_valid_number("Project choice: ", len(projects) + 1, MINIMUM_NUMBER)
    selected_project = projects[project_choice]
    print(selected_project)
    new_percentage = get_valid_number("New percentage: ", PERCENTAGE_THRESHOLD, MINIMUM_NUMBER)
    new_priority = get_valid_number("New priority: ", PRIORITY_THRESHOLD, MINIMUM_NUMBER)
    selected_project.update_project(new_priority, new_percentage)


def get_valid_number(prompt, high, low):
    try:
        number = int(input(prompt))
        if number < low or number > high:
            print("Invalid number")
            number = int(input(prompt))
    except ValueError:
        return ""
    return number


main()
