from script_modules import datetime_handler, file_handler, todoist_data_fetcher, program_commands
import datetime
import json
import sys


class App:
    def __init__(self):
        self.VERBOSE = False
        file = open(file_handler.personal_data_filename, "r")
        self.user_data = json.load(file)
        file.close()
        self.all_current_projects = []
        self.all_current_sections = []
        self.all_current_tasks = []


def print_help_menu():
    print("shift today/tomorrow +/-HH:MM\t\t" +
          "Moves the schedule for the day by the amount of time given, making it earlier(-) or later(+).")


# Main program logic follows:
if __name__ == '__main__':
    mainApp = App()
    print('Running Todoist script ...')

    if len(sys.argv) < 2:
        print_help_menu()
        exit()

    if sys.argv[1] == 'sync':
        if sys.argv[2] == '-v':
            mainApp.VERBOSE = True
        program_commands.sync_all_data_command(mainApp)
    elif sys.argv[1] == 'save':
        program_commands.save_all_data_command(mainApp)
    elif sys.argv[1] == 'shift':
        if sys.argv[3] == '-v':
            mainApp.VERBOSE = True
        program_commands.sync_all_data_command(mainApp)
        program_commands.shift_command(mainApp, sys.argv[2])

    mainApp.VERBOSE = True
    program_commands.sync_all_data_command(mainApp)
    task_list = program_commands.get_all_tasks_due_today(mainApp.all_current_tasks)
    for task in task_list:
        if task.due is not None:
            print("\nTask => " + task.content)
            datetime_handler.get_datetime_in_due_string_format(task.due_string, "+1")
