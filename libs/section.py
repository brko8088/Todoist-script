class Section:
    def __init__(self, todoist_section):
        self.id = todoist_section.get("id")
        self.project_id = todoist_section.get("project_id")
        self.name = todoist_section.get("name")
        self.order = todoist_section.get("order")
    
    def to_string(self):
        print("ID ============> " + str(self.id))
        print("Project Id ====> " + str(self.project_id))
        print("Name ==========> " + str(self.name))
        print("Order =========> " + str(self.order))

        
    def generate_section_data_from_todoist(token, project_Id, sections_data):
        for section_Object in raw_section_data:
            sections_data.append(section_object.Section(section_Object))

        return sections_data