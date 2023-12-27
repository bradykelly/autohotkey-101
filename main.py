import os
import json
from common.constants import CONFIG_FILE_PATH


def get_all_projects_todos(projects_folder: str):
    """
    Get all projects and their todos from the projects folder
    :param projects_folder: the path to the projects folder
    :return: a list of projects and their todos
    """

    projects = os.listdir(projects_folder)
    projects_todos = []
    for project in projects:
        project_todos = []
        project_path = os.path.join(projects_folder, project)
        if os.path.isdir(project_path):
            todos = os.listdir(project_path)
            for todo in todos:
                todo_path = os.path.join(project_path, todo)
                if os.path.isfile(todo_path):
                    project_todos.append(todo)
        projects_todos.append((project, project_todos))
    return projects_todos


def read_file_extensions(language: str):
    """
    Read the file extensions from the "source_extensions" section of a
     JSON config file global to the project with many sections.

     :throws: FileNotFoundError if the JSON file does not exist
    :return: a list of file extensions.
    """

    with open(CONFIG_FILE_PATH, "r") as config_file:
        config = json.load(config_file)
        return config["source_extensions"]