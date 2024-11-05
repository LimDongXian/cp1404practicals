"""
Project Management
Estimate: 30 minutes
Actual:    minutes
"""
from prac_07.project import Project


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_file()
    display_projects(projects)


def load_file():
    projects = []
    with open('projects.txt', 'r') as in_file:
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
