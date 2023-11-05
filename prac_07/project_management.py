"""

Estimate: 120 minutes
Actual: 109 so far... + 20 -> 129 minutes
"""
import datetime
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
            filter_projects_by_date(projects)
        elif user_choice == "a":
            add_new_project(projects)
        elif user_choice == "u":
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        user_choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    projects.sort()
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


def filter_projects_by_date(projects):
    """Print projects that start after user-specified date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date_to_filter_by = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects_filtered_by_date = sorted([project for project in projects if
                                        datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() >=
                                        date_to_filter_by])
    print("Projects that start after the specified date:")
    for project in projects_filtered_by_date:
        print(project)


def add_new_project(projects):
    """Add new project to projects list."""
    print("Lets add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    """Update priority and or percentage of user-selected project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_to_update_index = int(input("Project choice: "))
    project_to_update = projects[project_to_update_index]
    print(project_to_update)

    new_percentage = input("New percentage: ")
    if new_percentage == "":
        new_percentage = project_to_update.completion_percentage
    else:
        project_to_update.completion_percentage = int(new_percentage)

    new_priority = input("New priority: ")
    if new_priority == "":
        new_priority = project_to_update.priority
    else:
        project_to_update.priority = int(new_priority)


def test_functions():
    """Test other functions."""
    # Test load_projects_from_file function
    projects = load_projects_from_file(DEFAULT_FILENAME)
    for project in projects:
        print(project)
    #


if __name__ == '__main__':
    main()
