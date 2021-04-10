import todoist_manager
import requests
import file_manager
import datetime
import json
import uuid
import sys

VERBOSE = False;


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


def get_processed_datetime(date_time, shift_value):
    print(date_time)
    print(shift_value)

    # Splitting Date Formats
    time_to_process = date_time[11:-1].split(":")
    print(time_to_process)

    time_to_add = shift_value[1:].split(":")
    print(time_to_add)

    hours_time_to_add = int(time_to_process[0]) + int(time_to_add[0])
    print(hours_time_to_add)
    minutes_time_to_add = int(time_to_process[1]) + int(time_to_add[1])
    print(minutes_time_to_add)
    seconds_time_to_add = int(time_to_process[2]) + int(time_to_add[2])
    print(minutes_time_to_add)

    new_datetime = date_time[:11] +  + time_to_process[1] + time_to_process[2] + "Z"
    return str(new_datetime)


def shift(task, token, shift_value):
    requests.post(
        "https://api.todoist.com/rest/v1/tasks/" + str(task.id),
        data=json.dumps({
            "due_datetime": str(get_processed_datetime(task.due_datetime, shift_value)),
        }),

        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer %s" % token
        })


def sync_data():
    all_current_projects = todoist_manager.generate_project_data_from_todoist(
        mainApp.user_data.get("token"), mainApp.all_current_projects)

    if VERBOSE:
        print("All Projects Loaded")
    x = 1

    for project in all_current_projects:
        all_current_sections = todoist_manager.generate_section_data_from_todoist(
            mainApp.user_data.get("token"), project.id, mainApp.all_current_sections)

        all_current_tasks = (todoist_manager.generate_task_data_from_todoist(
            mainApp.user_data.get("token"), project.id, mainApp.all_current_tasks))

        if VERBOSE:
            print("Loaded Sections and Tasks from Project " + str(x) + " out ot " + str(len(all_current_projects)))
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
    # if len(sys.argv) < 2:
    #     print_help_menu()
    #     exit()

    # if sys.argv[1] == 'sync':
    #     if sys.argv[2] == '-v':
    #         VERBOSE == True
    #     sync_data();
    # elif sys.argv[1] == 'save':
    #     save_data();
    # elif sys.argv[1] == 'shift':
    #     shift(mainApp.all_current_tasks[0], mainApp.user_data.get("token"), sys.argv[2])

    # VERBOSE = True;
    # sync_data()
    #
    # tasks_for_today = get_tasks_for_today(mainApp.all_current_tasks)

    # shift(mainApp.all_current_tasks[0], mainApp.user_data.get("token"), "+02:00")

    print(get_processed_datetime("2021-04-11T01:30:00Z", "+02:00"))

    # for task in tasks_for_today:
    #     print(task.due_datetime)


