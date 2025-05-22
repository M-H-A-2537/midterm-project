import os
import shutil


#<<<<<<< Our classes >>>>>>>
""",,,,,,,FOLDER MAKER,,,,,,,"""
class Folder_maker :
    def __init__(self, folder_path : str, name : str) :
        self.now_path = os.getcwd()
        self.folder_path = folder_path
        self.name = name

    def make_folder (self) :
        os.chdir(self.folder_path)
        os.makedirs(self.name)
        os.chdir(self.now_path)
        if os.path.exists(self.folder_path + f"/{self.name}"):
            print(f"{self.name} folder was created successfully.")


""",,,,,,,FOLDER DELETER,,,,,,,"""
class Folder_deleter :
    def __init__(self, folder_path : str, name : str) :
        self.now_path = os.getcwd()
        self.folder_path = folder_path
        self.name = name

    def delete_folder (self) :
        os.chdir(self.folder_path)
        os.rmdir(self.name)
        os.chdir(self.now_path)
        if not os.path.exists(self.folder_path + f"/{self.name}"):
            print(f"{self.name} folder was deleted successfully.")


""",,,,,,,FILE MAKER,,,,,,,"""
class File_maker :
    def __init__(self, folder_path : str, name : str) :
        self.now_path = os.getcwd()
        self.folder_path = folder_path
        self.name = name

    def make_file (self) :
        os.chdir(self.folder_path)
        open(self.name, "w").close()
        os.chdir(self.now_path)
        if os.path.exists(self.folder_path + f"/{self.name}"):
            print(f"{self.name} file was created successfully.")


""",,,,,,,FILE DELETER,,,,,,,"""
class File_deleter :
    def __init__(self, folder_path : str, name : str) :
        self.now_path = os.getcwd()
        self.folder_path = folder_path
        self.name = name

    def delete_file (self) :
        os.chdir(self.folder_path)
        os.remove(self.name)
        os.chdir(self.now_path)
        if not os.path.exists(self.folder_path + f"/{self.name}"):
            print(f"{self.name} file was deleted successfully.")


""",,,,,,,NAVIGATION,,,,,,,"""
class Navigation :
    def __init__(self, new_path : str) :
        self.new_path = new_path

    def movement(self) :
        os.chdir(self.new_path)


""",,,,,,,FILE EDITOR,,,,,,,"""
class File_editor :
    def __init__(self, file_path, name) :
        self.file_path = file_path
        self.now_path = os.getcwd()
        self.name = name

    def newfile (self) :
        os.chdir(self.file_path)
        Text = []
        print("(Print %END% to finish your work.)")
        while True :
            line = input()
            if line == "%END%" :
                break
            Text.append(line)
        f = open(self.name, "w")
        for text in Text :
            f.write(text + "\n")
        f.flush()
        f.close()
        os.chdir(self.now_path)

    def append (self):
        os.chdir(self.file_path)
        Text = []
        print("(Print %END% to finish your work.)")
        while True:
            line = input()
            if line == "%END%" :
                break
            Text.append(line)
        f = open(self.name, "a")
        for text in Text:
            f.write(text + "\n")
        f.close()
        os.chdir(self.now_path)


""",,,,,,,TEXT EDITOR,,,,,,,"""
class Text_editor :
    def __init__(self, name : str, text_path : str, line : int, text = str()) :
        self.text_path = text_path
        self.now_path = os.getcwd()
        self.line = line
        self.text = text
        self.name = name

    def edit_line(self):
        os.chdir(self.text_path)
        f = open(self.name, "r")
        Text = f.readlines()
        Text[self.line - 1] = self.text + "\n"
        f.close()
        f = open(self.name, "w")
        for txt in Text :
            f.write(txt)
        f.flush()
        f.close()
        os.chdir(self.now_path)

    def delete_line(self) :
        os.chdir(self.text_path)
        f = open(self.name, "r")
        Text = f.readlines()
        Text.pop(self.line - 1)
        f.close()
        f = open(self.name, "w")
        for txt in Text:
            f.write(txt)
        f.flush()
        f.close()
        os.chdir(self.now_path)


""",,,,,,,TEXT READER,,,,,,,"""
class Text_reader :
    def __init__(self, name, text_path) :
        self.text_path = text_path
        self.name = name
        self.now_path = os.getcwd()

    def read(self) :
        os.chdir(self.text_path)
        f = open(self.name, "r")
        Text = f.readlines()
        f.close()
        for text in Text :
            print(text, end="")
        os.chdir(self.now_path)


""",,,,,,,IN_NEW_PLACE,,,,,,,"""
class In_new_place :
    def __init__(self, source_path : str, destination_path : str) :
        self.source_path = source_path
        self.destination_path = destination_path

    def cut(self) :
        shutil.move(self.source_path, self.destination_path)

    def copy(self) :
        shutil.copy2(self.source_path, self.destination_path)


""",,,,,,,RENAME,,,,,,,"""
class Rename :
    def __init__(self, old_name : str, new_name : str, path_in_folder : str) :
        self.old_name = old_name
        self.new_name = new_name
        self.now_path = os.getcwd()
        self.path_in_folder = path_in_folder

    def rename (self) :
        os.chdir(self.path_in_folder)
        os.rename(self.old_name, self.new_name)
        os.chdir(self.now_path)