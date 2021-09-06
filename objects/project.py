class Project:
    def __init__(self, todoist_project):
        self.id = todoist_project.get("id")
        self.color = todoist_project.get("color")
        self.name = todoist_project.get("name")
        self.comment_count = todoist_project.get("comment_count")
        self.shared = todoist_project.get("shared")
        self.favorite = todoist_project.get("favorite")
        self.sync_id = todoist_project.get("sync_id")
        self.url = todoist_project.get("url")
        self.order = todoist_project.get("order")
        self.inbox_project = todoist_project.get("inbox_project")
        self.parent = todoist_project.get("parent")
        self.parent_id = todoist_project.get("parent_id")

    def load_request_in_memory(self, project_data):
        for project_Object in project_data:
            project_data.append(Project(project_Object))

        return project_data