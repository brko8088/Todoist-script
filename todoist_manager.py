import project_object
import section_object
import task_object
import requests


def get_todoist_projects(token):
    output = requests.get("https://api.todoist.com/rest/v1/projects",
                          headers={"Authorization": "Bearer " + token}).json()
    return output


def get_todoist_sections(token, project_Id):
    output = requests.get("https://api.todoist.com/rest/v1/sections?project_id=" + str(project_Id),
                          headers={"Authorization": "Bearer " + token}).json()
    return output


def get_todoist_tasks(token, project_Id):
    output = requests.get("https://api.todoist.com/rest/v1/tasks",
                          params={"project_id": project_Id},
                          headers={"Authorization": "Bearer " + token}).json()
    return output


def fetched_project_data_from_todoist(token):
    raw_project_data = get_todoist_projects(token)
    projects = []
    for project_Object in raw_project_data:
        projects.append(project_object.Project(project_Object))
    return projects


def fetched_section_data_from_todoist(token, project_Id):
    raw_section_data = get_todoist_sections(token, project_Id)
    sections = []
    for section_Object in raw_section_data:
        sections.append(section_object.Section(section_Object))
    return sections


def fetched_task_data_from_todoist(token, project_Id):
    raw_tasks_data = get_todoist_tasks(token, project_Id)
    tasks = []
    for task_Object in raw_tasks_data:
        tasks.append(task_object.Task(task_Object))
    return tasks
