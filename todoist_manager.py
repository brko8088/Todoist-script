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


def generate_project_data_from_todoist(token, project_data):
    raw_project_data = get_todoist_projects(token)

    for project_Object in raw_project_data:
        project_data.append(project_object.Project(project_Object))
        return project_data


def generate_section_data_from_todoist(token, project_Id, sections_data):
    raw_section_data = get_todoist_sections(token, project_Id)

    for section_Object in raw_section_data:
        sections_data.append(section_object.Section(section_Object))
        return sections_data


def generate_task_data_from_todoist(token, project_Id, task_data):
    raw_tasks_data = get_todoist_tasks(token, project_Id)

    for task_Object in raw_tasks_data:
        task_data.append(task_object.Task(task_Object))
        return task_data
