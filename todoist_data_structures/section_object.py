class Section:
    def __init__(self, todoist_section):
        self.id = todoist_section.get("id")
        self.project_id = todoist_section.get("project_id")
        self.name = todoist_section.get("name")
        self.order = todoist_section.get("order")