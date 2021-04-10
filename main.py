import todoist_manager
import requests
import file_manager
import datetime
import json
import sys
import uuid


class App:
    def __init__(self):
        file = open(file_manager.personal_data_filename, "r")
        self.user_data = json.load(file)
        file.close()


def print_help_menu():
    print("shift today/tomorrow +/-HH:MM\t\t" +
          "Moves the schedule for the day by the amount of time given, making it earlier(-) or later(+).")


def get_tasks_for_today(tasks):
    tasks_for_the_day = []
    print(datetime.datetime.now().date())
    for task_list in tasks:
        for task_item in task_list:
            if task_item is not None:
                print(task.due_date)
                if str(task.due_date) == str(datetime.datetime.now().date()):
                    tasks_for_today.append(task)
    return tasks_for_the_day


def shift(tasks, token):
    requests.post(
        "https://api.todoist.com/rest/v1/tasks/" + str(tasks[0].id),
        data=json.dumps({
            "due_string": "everyday at 11:00",
            "due_date": "2021-04-09"}),

        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer %s" % token
        })


# Main program logic follows:
if __name__ == '__main__':

    mainApp = App()

    current_projects = todoist_manager.fetched_project_data_from_todoist(
        mainApp.user_data.get("token"))

    # current_sections = todoist_manager.fetched_section_data_from_todoist(
    #     mainApp.user_data.get("token"), current_projects[1].id)

    all_current_tasks = []
    for project in current_projects:
        all_current_tasks.append(todoist_manager.fetched_task_data_from_todoist(
            mainApp.user_data.get("token"), project.id))

    tasks_for_today = get_tasks_for_today(all_current_tasks)

    for task in tasks_for_today:
        print(task.content)
    # print('Running todoist script ... ')
    # if len(sys.argv) < 2:
    #     print_help_menu()
    #     exit()
    #
    # if sys.argv[1] == 'shift':
    #     shift(current_tasks, mainApp.user_data.get("token"))
    # elif sys.argv[1] == 'Ultrasonic':
    #     test_Ultrasonic()
    # elif sys.argv[1] == 'Servo':
    #     test_Servo()
    # elif sys.argv[1] == 'ADC':
    #     test_Adc()
    # elif sys.argv[1] == 'Buzzer':
    #     test_Buzzer()




