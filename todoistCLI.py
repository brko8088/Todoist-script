from todoist_libraries import datetime_handler, file_handler, program_commands
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
    print("shift today/tomorrow +/-HH:MM")
    print("\t\tMoves the schedule for the day by the amount of time given, making it earlier(-) or later(+).")
    print("spawn [number] [task_name] [parent_project] [parent_section] [due_string]")
    print("")


def turn_argument_into_readable_string(argument):
    argument_list = argument.split("_")
    x = 0
    for word in argument_list:
        if x == 0:
            text = word
        else:
            text = text + " " + word
        x = x + 1
    return text


# Main program logic follows:
if __name__ == '__main__':
    mainApp = App()
    print('Running Todoist script ...')

    if len(sys.argv) < 2:
        print_help_menu()
        exit()

    for arg in sys.argv:
        print(arg)

    if sys.argv[1] == 'help' or sys.argv[1] == '-h':
        print_help_menu()

    elif sys.argv[1] == 'sync':
        if sys.argv[2] == '-v':
            mainApp.VERBOSE = True
        program_commands.load_all_project_data_command(mainApp)

    elif sys.argv[1] == 'save':
        program_commands.save_all_data_command(mainApp)

    elif sys.argv[1] == 'shift':
        if sys.argv[3] == '-v':
            mainApp.VERBOSE = True
        program_commands.load_all_project_data_command(mainApp)
        program_commands.shift_command(mainApp, sys.argv[2])

    elif sys.argv[1] == 'spawn':
        program_commands.load_all_project_data_command(mainApp)
        mainApp.VERBOSE = True
        if sys.argv[2] == '-t':
            amount = sys.argv[3]
            project = turn_argument_into_readable_string(sys.argv[5])
            program_commands.load_all_sections_from_project(mainApp, project)
            section = turn_argument_into_readable_string(sys.argv[6])
            program_commands.load_all_tasks_from_section(mainApp, section)
            task_name = turn_argument_into_readable_string(sys.argv[4])
            due_string = turn_argument_into_readable_string(sys.argv[7])
            program_commands.create_tasks(mainApp, amount, task_name, project, section, due_string)

        if sys.argv[2] == '-p':
            project_name = turn_argument_into_readable_string(sys.argv[3])
            parent_project = turn_argument_into_readable_string(sys.argv[4])

        if sys.argv[2] == '-s':
            section_name = turn_argument_into_readable_string(sys.argv[3])
            parent_project = turn_argument_into_readable_string(sys.argv[4])

    elif sys.argv[1] == 'test_tasks':
        mainApp.VERBOSE = True
        program_commands.load_all_project_data_command(mainApp)
        task_list = program_commands.get_all_tasks_due_today(mainApp.all_current_tasks)
        for task in task_list:
            if task.due is not None:
                print("\nTask => " + task.content)
                datetime_handler.get_datetime_in_due_string_format(task.due_string, "+1")


