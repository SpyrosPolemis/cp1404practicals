"""

Estimate: 120 minutes
Actual:
"""
# import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """"""
    projects = load_projects_from_file(DEFAULT_FILENAME)
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "l":
            filename_to_load = input("Enter filename: ")
            projects = load_projects_from_file(filename_to_load)
        elif user_choice == "s":
            filename_to_write = input("Enter filename: ")
            save_projects_to_file(filename_to_write, projects)
        elif user_choice == "d":
            display_projects(projects)
        elif user_choice == "f":
            pass
        elif user_choice == "a":
            pass
        elif user_choice == "u":
            pass
        else:
            print("Invalid input")
        print(MENU)
        user_choice = input(">>> ").lower()


def display_projects(projects):
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    print("Incomplete projects:")
    for project in projects:
        if project not in complete_projects:
            print(f"  {project}")
    print("Complete projects:")
    for complete_project in complete_projects:
        print(f"  {complete_project}")


def load_projects_from_file(filename):
    """Load projects from selected """
    projects = []
    with open(filename) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects_to_file(filename, projects):
    """Save projects to selected file."""
    with open(filename, "w") as out_file:
        print("Name    Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(repr(project), file=out_file)


def test_functions():
    """Test other functions."""
    # Test load_projects_from_file function
    projects = load_projects_from_file(DEFAULT_FILENAME)
    for project in projects:
        print(project)
    #


if __name__ == '__main__':
    main()
