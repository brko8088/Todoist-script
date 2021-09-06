from libs import todoist_data_get, todoist_data_post, datetime_handler, file_handler
import datetime
# Program Commands


def get_all_tasks_due_today(tasks):
    tasks_for_the_day = []

    for task_item in tasks:
        if task_item.due is not None:
            if str(task_item.due_date) == str(datetime.datetime.now().date()):
                tasks_for_the_day.append(task_item)

    return tasks_for_the_day


def shift_command(mainApp, user_input_shift_value):
    tasks_for_today = get_all_tasks_due_today(mainApp.all_current_tasks)

    for task_item in tasks_for_today:
        print("\nTask => " + task_item.content)
        datetime_handler.shift_schedule(mainApp.user_data.get("token"), task_item, user_input_shift_value)


def load_all_project_data_command(mainApp):
    mainApp.all_current_projects = todoist_data_get.generate_project_data_from_todoist(
        mainApp.user_data.get("token"), mainApp.all_current_projects)

    if mainApp.VERBOSE:
        print("All Projects Loaded")



def save_all_data_command(mainApp):
    if len(mainApp.all_current_projects) == 0:
        print("Project size is 0")
        print("No elements have been synced or loaded...")
    else:
        file_handler.save_data_to_json(file_handler.personal_projects_filename, mainApp.all_current_projects)

    if len(mainApp.all_current_sections) == 0:
        print("Section size is 0")
        print("No elements have been synced or loaded...")
    else:
        file_handler.save_data_to_json(file_handler.personal_sections_filename, mainApp.all_current_sections)

    if len(mainApp.all_current_tasks) == 0:
        print("Task size is 0")
        print("No elements have been synced or loaded...")
    else:
        file_handler.save_data_to_json(file_handler.personal_task_filename, mainApp.all_current_tasks)


def create_tasks(mainApp, amount, task_name, project_name, section_name, due_string):
    token = mainApp.user_data.get("token")
    project_id = "0"
    section_id = "0"

    for project in mainApp.all_current_projects:
        if project.name == project_name:
            project_id = project.id

    for section in mainApp.all_current_sections:
        if section.name == section_name and section.project_id == project_id:
            section_id = section.id

    number_of_existing_tasks = 0

    for task in mainApp.all_current_tasks:
        if task.section_id == section_id:
            temp_task_name_list_1 = task.content.split(" ")
            temp_task_name_list_2 = task_name.split(" ")

            i = 0
            for frag in temp_task_name_list_2:
                are_they_the_same = True
                if frag != temp_task_name_list_1[i]:
                    are_they_the_same = False
                i = i + 1
            if are_they_the_same:
                number_of_existing_tasks += 1

    for x in range (1 + number_of_existing_tasks, int(amount) + number_of_existing_tasks + 1):
        todoist_data_post.create_task(token, task_name + " " + str(x), project_id, section_id, due_string)
        due_string = datetime_handler.get_datetime_in_due_string_format(due_string, "+00:30")


def load_all_sections_from_project(mainApp, project_name):
    for project_iterator in mainApp.all_current_projects:
        if project_iterator.name == project_name:
            mainApp.all_current_sections = todoist_data_get.generate_section_data_from_todoist(
                mainApp.user_data.get("token"), project_iterator.id, mainApp.all_current_sections)

    if mainApp.VERBOSE:
        print("Loaded all sections from Project " + str(project_name))


def load_all_tasks_from_section(mainApp, section_name):
    for section_iterator in mainApp.all_current_sections:
        if section_iterator.name == section_name:
            mainApp.all_current_tasks = (todoist_data_get.generate_task_data_from_todoist(
                mainApp.user_data.get("token"), section_iterator.id, mainApp.all_current_tasks))

    if mainApp.VERBOSE:
        print("Loaded all tasks from Section " + str(section_name))