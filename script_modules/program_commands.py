import todoist_data_fetcher
import datetime_handler
import file_handler
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


def sync_all_data_command(mainApp):
    mainApp.all_current_projects = todoist_data_fetcher.generate_project_data_from_todoist(
        mainApp.user_data.get("token"), mainApp.all_current_projects)

    if mainApp.VERBOSE:
        print("All Projects Loaded")
    x = 1

    for project in mainApp.all_current_projects:
        mainApp.all_current_sections = todoist_data_fetcher.generate_section_data_from_todoist(
            mainApp.user_data.get("token"), project.id, mainApp.all_current_sections)

        mainApp.all_current_tasks = (todoist_data_fetcher.generate_task_data_from_todoist(
            mainApp.user_data.get("token"), project.id, mainApp.all_current_tasks))

        if mainApp.VERBOSE:
            print("Loaded Sections and Tasks from Project " + str(x) +
                  " out ot " + str(len(mainApp.all_current_projects)))
            x += 1


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