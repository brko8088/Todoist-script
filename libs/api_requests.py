from todoist_data_structures import task_object, section_object, project_object
import requests, json, uuid

VERBOSE = False


def get_all_projects(token):
    output = requests.get("https://api.todoist.com/rest/v1/projects",
                          headers={"Authorization": "Bearer " + token}).json()
    return output


def get_project_sections(token, project_id):
    output = requests.get("https://api.todoist.com/rest/v1/sections?project_id=" + str(project_id),
                          headers={"Authorization": "Bearer " + token}).json()
    return output


def get_project_tasks(token, project_id):
    output = requests.get("https://api.todoist.com/rest/v1/tasks",
                          params={"project_id": project_id},
                          headers={"Authorization": "Bearer " + token}).json()
    return output


def create_task(token, task_content, project_id, section_id = "", due_string = ""):
    requests.post(
        "https://api.todoist.com/rest/v1/tasks",
        data=json.dumps({
            "content": str(task_content),
            "project_id": int(project_id),
            "section_id": int(section_id),
            "due_string": str(due_string),
            "due_lang": "en",
            "priority": 4
        }),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer %s" % token
        }).json()

