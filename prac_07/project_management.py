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
            project = Project(part[0], part[1], part[2], part[3], part[4])
            projects.append(project)
        return projects


def display_projects(projects):
    for project in projects:
        print(project)


main()
