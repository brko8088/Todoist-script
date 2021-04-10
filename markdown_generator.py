class MarkdownGenerator:
    def __init__(self, test_directory, test_filename):
        file_opener = open(test_directory + test_filename, "c")
        file_opener.close()

    # def insert_text_at(self):

# Code to build the Markdown generator extension
# I've left this here for when I decide to consider building it.
#
# test_directory = "/Users/brunokoppel/.sj/04 Project (Building the Foundations)/07 Epic (The Spring Semester)/"
# test_filename = "Sprint_test.md"
#
# tree_file = file_manager.Directory(mainApp.user_data.get("main_scrum_directory"))
# for project_directory in tree_file.sub_directories:
#     print(project_directory.directory_path + " Subdirectories:")
#     if project_directory.directory_path[-4:] != ".git":
#         for epic_directory in project_directory.sub_directories:
#             print(epic_directory.directory_path)
#
# sp = markdown_generator.markdown_generator(test_directory,test_filename)
