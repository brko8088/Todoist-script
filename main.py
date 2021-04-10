import todoist_manager
import file_manager
import datetime_handler
import datetime
import json
import sys
import os

VERBOSE = False


class App:
    def __init__(self):
        file = open(file_manager.personal_data_filename, "r")
        self.user_data = json.load(file)
        file.close()
        self.all_current_projects = []
        self.all_current_sections = []
        self.all_current_tasks = []


def print_help_menu():
    print("shift today/tomorrow +/-HH:MM\t\t" +
          "Moves the schedule for the day by the amount of time given, making it earlier(-) or later(+).")


def get_tasks_for_today(tasks):
    tasks_for_the_day = []

    for task_item in tasks:
        if task_item.due is not None:
            if str(task_item.due_date) == str(datetime.datetime.now().date()):
                tasks_for_the_day.append(task_item)

    return tasks_for_the_day


def shift(user_input_shift_value):
    tasks_for_today = get_tasks_for_today(mainApp.all_current_tasks)

    for task_item in tasks_for_today:
        print("\nTask => " + task_item.content)
        datetime_handler.shift(mainApp.user_data.get("token"), task_item, user_input_shift_value)


def sync_data():
    mainApp.all_current_projects = todoist_manager.generate_project_data_from_todoist(
        mainApp.user_data.get("token"), mainApp.all_current_projects)

    if VERBOSE:
        print("All Projects Loaded")
    x = 1

    for project in mainApp.all_current_projects:
        mainApp.all_current_sections = todoist_manager.generate_section_data_from_todoist(
            mainApp.user_data.get("token"), project.id, mainApp.all_current_sections)

        mainApp.all_current_tasks = (todoist_manager.generate_task_data_from_todoist(
            mainApp.user_data.get("token"), project.id, mainApp.all_current_tasks))

        if VERBOSE:
            print("Loaded Sections and Tasks from Project " + str(x) +
                  " out ot " + str(len(mainApp.all_current_projects)))
            x += 1


def save_data():
    if len(mainApp.all_current_projects) == 0:
        print("Project size is 0")
        print("No elements have been synced or loaded...")
    else:
        file_manager.save_data_to_json(file_manager.personal_projects_filename, mainApp.all_current_projects)

    if len(mainApp.all_current_sections) == 0:
        print("Section size is 0")
        print("No elements have been synced or loaded...")
    else:
        file_manager.save_data_to_json(file_manager.personal_sections_filename, mainApp.all_current_sections)

    if len(mainApp.all_current_tasks) == 0:
        print("Task size is 0")
        print("No elements have been synced or loaded...")
    else:
        file_manager.save_data_to_json(file_manager.personal_task_filename, mainApp.all_current_tasks)


# Main program logic follows:
if __name__ == '__main__':
    mainApp = App()
    print('Running Todoist script ...')

    if len(sys.argv) < 2:
        print_help_menu()
        exit()

    if sys.argv[1] == 'sync':
        if sys.argv[2] == '-v':
            VERBOSE = True
        sync_data()
    elif sys.argv[1] == 'save':
        save_data()
    elif sys.argv[1] == 'shift':
        if sys.argv[3] == '-v':
            VERBOSE = True
        sync_data()
        shift(sys.argv[2])

    # VERBOSE = True
    # sync_data()
    # task_list = get_tasks_for_today(mainApp.all_current_tasks)
    # for task in task_list:
    #     if task.due is not None:
    #         print("\nTask => " + task.content)
    #         datetime_handler.get_processed_string(task.due_string, "+1")
