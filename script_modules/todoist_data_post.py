import requests
import json
import uuid


def create_task(token, task_content, project_id, section_id, due_string):
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

