"""
Project Management
Estimate: 30 minutes
Actual:    minutes
"""
from prac_07.project import Project

MENU = ("- (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by dat\n"
        " - (A)dd new project\n - (U)pdate project\n - (Q)uit")
FILENAME = "projects.txt"


def main():
    projects = load_file()
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Loaded projects")
        if choice == "S":
            print("Save projects")
        if choice == "D":
            display_projects(projects)
        if choice == "F":
            print("Filter projects by dat")
        if choice == "A":
            print("Add new project")
        if choice == "U":
            print("Update project")
        else:
            print("Invalid Choice")
            choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_file():
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            part = line.strip().split("	")
            project = Project(str(part[0]), part[1], int(part[2]), float(part[3]), int(part[4]))
            projects.append(project)
        return projects


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]
    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)
    print("Completed projects:")
    for project in sorted(completed_projects):
        print(project)


main()
