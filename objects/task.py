class Task:
    def __init__(self, todoist_task):
        self.id = todoist_task.get("id")
        self.project_id = todoist_task.get("project_id")
        self.section_id = todoist_task.get("section_id")
        self.parent_id = todoist_task.get("parent_id")
        self.content = todoist_task.get("content")
        self.comment_count = todoist_task.get("comment_count")
        self.assignee = todoist_task.get("assignee")
        self.assigner = todoist_task.get("assigner")
        self.order = todoist_task.get("order")
        self.priority = todoist_task.get("priority")
        self.url = todoist_task.get("url")
        self.due = todoist_task.get("due")
        if self.due is not None:
            self.due_recurring = self.due.get("recurring")
            self.due_date = self.due.get("date")
            self.due_datetime = self.due.get("datetime")
            self.due_string = self.due.get("string")
            self.due_timezone = self.due.get("timezone")

        

    def generate_task_data_from_todoist(token, project_Id, task_data):
        raw_tasks_data = get_project_tasks(token, project_Id)

        for task_Object in raw_tasks_data:
            task_data.append(task_object.Task(task_Object))

        return task_data