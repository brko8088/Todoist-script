import os

personal_data_filename = ".data/.api_data.json"


class Directory:
    def __init__(self, path_given):
        self.directory_path = path_given
        self.sub_directories = [Directory(f.path) for f in os.scandir(path_given) if f.is_dir()]




