import json
import os

personal_data_filename_from_sm = "../.data/api_data.json"
personal_projects_filename_from_sm = "../.data/project_data.json"
personal_sections_filename_from_sm = "../.data/section_data.json"
personal_task_filename_from_sm = "../.data/task_data.json"

personal_data_filename = ".data/api_data.json"
personal_projects_filename = ".data/project_data.json"
personal_sections_filename = ".data/section_data.json"
personal_task_filename = ".data/task_data.json"


class Directory:
    def __init__(self, path_given):
        self.directory_path = path_given
        self.sub_directories = [Directory(f.path) for f in os.scandir(path_given) if f.is_dir()]


def save_data_to_json(filename, data):
    full_string_output = ""

    for obj in data:
        json_string = json.dumps(obj.__dict__)
        full_string_output += json_string

    with open(filename, 'w') as json_file:
        json.dump(full_string_output, json_file)
