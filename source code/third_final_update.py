import os
import sys
import shutil
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QFont

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


#<<<<<<< Our functions >>>>>>>
def path_maker(full_path : str) :
    path = str()
    global base_path
    if full_path[0:2] != "//" :
        full_path_list = full_path.split('/')
        if len(full_path_list) > 1 :
            path = '/'.join(full_path_list)
        else :
            path = full_path_list[0]
    else :
        if unix_path == "//" :
            pass
        else:
            path = unix_path[2:1]
    new_path = base_path + "/" + path
    now_path = os.getcwd()
    try :
        os.chdir(new_path)
    except FileNotFoundError :
        print("\33[31mThe given path was not found.\33[0m")
        return None
    os.chdir(now_path)
    return new_path

def windows_path_maker(full_path : str) :
    global windows_path
    windows_first = windows_path
    path = windows_path
    if full_path[0:3] != "C:/" :
        path = path + '/' + full_path
        try:
            os.chdir(path)
        except FileNotFoundError:
            print("\33[31mThe given path was not found.\33[0m")
            return None
        os.chdir(windows_first)
        return path
    else :
        path = full_path
        try :
            os.chdir(path)
        except FileNotFoundError :
            print("\33[31mThe given path was not found.\33[0m")
            return None
        os.chdir(windows_first)
        return path

def Linked_function(commends : list) :
    global unix_path
    global windows_path
    global base_path
    global cm
    match commends[0] :
#,,,,,mkdir,,,,,#
        case "mkdir" :
            if len(commends) == 2 :
                folder = Folder_maker(windows_path, commends[1])
                folder.make_folder()
            elif len(commends) == 3 :
                folder_path = None
                if cm == '$' :
                    folder_path = path_maker(commends[1])
                else :
                    folder_path = windows_path_maker(commends[1])
                if folder_path == None :
                    return True
                folder = Folder_maker(folder_path, commends[2])
                folder.make_folder()
            return True
#,,,,,rm,,,,,#
        case "rm":
            folder_path = None
            path_list = commends[1].split('/')
            if len(path_list) == 1 :
                if commends[1][-4:] == ".txt":
                    file = File_deleter(windows_path, commends[1])
                    try :
                        file.delete_file()
                    except FileNotFoundError :
                        print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                    return True
                else:
                    folder = Folder_deleter(windows_path, commends[1])
                    try:
                        folder.delete_folder()
                    except OSError:
                        print(f"\33[31m< {commends[1]} > directory is not empty.\33[0m")
                    return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if name[-4:] == ".txt" :
                if cm == '$' :
                    folder_path = path_maker(commends[1])
                else:
                    folder_path = windows_path_maker(commends[1])
                if folder_path == None :
                    return True
                file = File_deleter(folder_path, name)
                try:
                    file.delete_file()
                except FileNotFoundError:
                    print(f"\33[31m< {name} > file was not found.\33[0m")
                    return True
            else :
                if cm == '$':
                    folder_path = path_maker(commends[1])
                else:
                    folder_path = windows_path_maker(commends[1])
                if folder_path == None :
                    return True
                folder = Folder_deleter(folder_path, name)
                try :
                    folder.delete_folder()
                except OSError :
                    print(f"\33[31m< {name} > directory is not empty.\33[0m")
            return True
#,,,,,touch,,,,,#
        case "touch":
            if len(commends) == 2 :
                file = File_maker(windows_path, commends[1])
                file.make_file()
            elif len(commends) == 3 :
                folder_path = None
                if cm == '$':
                    folder_path = path_maker(commends[1])
                else:
                    folder_path = windows_path_maker(commends[1])
                if folder_path == None :
                    return True
                file = File_maker(folder_path, commends[2])
                file.make_file()
            return True
#,,,,,cd..,,,,,#
        case "cd.." :
            folder_path = None
            if cm == '$' :
                if unix_path == "//" :
                    return True
                unix_folder_path = unix_path[2:-1]
                unix_path_list = unix_folder_path.split('/')
                unix_path_list.pop(-1)
                if len(unix_path_list) == 0 :
                    unix_path = "//"
                else :
                    unix_path = "//" + '/'.join(unix_path_list) + '/'
                folder_path_list = windows_path.split('/')
                folder_path_list.pop(-1)
                folder_path = '/'.join(folder_path_list)
                moving = Navigation(folder_path)
                moving.movement()
                windows_path_list = windows_path.split('/')
                windows_path_list.pop(-1)
                if len(windows_path_list) == 0 or len(windows_path_list) == 1 :
                    windows_path = "C:/"
                else :
                    windows_path = '/'.join(windows_path_list)
            else :
                if base_path in windows_path :
                    if unix_path != "//" :
                        unix_folder_path = unix_path[2:-1]
                        unix_path_list = unix_folder_path.split('/')
                        unix_path_list.pop(-1)
                        if len(unix_path_list) == 0:
                            unix_path = "//"
                        else:
                            unix_path = "//" + '/'.join(unix_path_list) + '/'
                if windows_path == "C:/" :
                    return True
                windows_path_list = windows_path.split('/')
                windows_path_list.pop(-1)
                if len(windows_path_list) == 1 or len(windows_path_list) == 0 :
                    folder_path = "C:/"
                else :
                    folder_path = '/'.join(windows_path_list)
                windows_path = folder_path
                moving = Navigation(folder_path)
                moving.movement()
            return True
#,,,,,cd,,,,,#
        case "cd":
            folder_path = None
            if cm == '$':
                folder_path = path_maker(commends[1])
                if folder_path == None:
                    return True
                unix_path = "//" + commends[1] + "/"
                windows_path = base_path + '/' + commends[1]
            else :
                folder_path = windows_path_maker(commends[1])
                if folder_path == None :
                    return True
                windows_path = folder_path
                if base_path in windows_path :
                    unix_path = "//" + windows_path.replace(base_path, "")[1:] + '/'
            moving = Navigation(folder_path)
            moving.movement()
            return True
#,,,,,newfiletxt,,,,,#
        case "newfiletxt":
            path_list = commends[1].split('/')
            if len(path_list) == 1 :
                file = File_editor(windows_path, commends[1])
                file.newfile()
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if cm == '$' :
                folder_path = path_maker(commends[1])
            else :
                folder_path = windows_path_maker(commends[1])
            if folder_path == None :
                return True
            file = File_editor(folder_path, name)
            file.newfile()
            return True
#,,,,,appendtxt,,,,,#
        case "appendtxt":
            path_list = commends[1].split('/')
            if len(path_list) == 1:
                file = File_editor(windows_path, commends[1])
                try :
                    file.append()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if cm == '$':
                folder_path = path_maker(commends[1])
            else:
                folder_path = windows_path_maker(commends[1])
            if folder_path == None:
                return True
            file = File_editor(folder_path, name)
            try :
                file.append()
            except FileNotFoundError:
                print(f"\33[31m< {name} > file was not found.\33[0m")
            return True
#,,,,,editline,,,,,#
        case "editline" :
            path_list = commends[1].split('/')
            if len(path_list) == 1:
                text = Text_editor(commends[1], windows_path, int(commends[2]), commends[3])
                try:
                    text.edit_line()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if cm == '$':
                folder_path = path_maker(commends[1])
            else:
                folder_path = windows_path_maker(commends[1])
            if folder_path == None:
                return True
            text = Text_editor(name, folder_path, int(commends[2]), commends[3])
            try:
                text.edit_line()
            except FileNotFoundError:
                print(f"\33[31m< {name} > file was not found.\33[0m")
            return True
#,,,,,deline,,,,,#
        case "deline":
            path_list = commends[1].split('/')
            if len(path_list) == 1:
                text = Text_editor(commends[1], windows_path, int(commends[2]))
                try:
                    text.delete_line()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if cm == '$':
                folder_path = path_maker(commends[1])
            else:
                folder_path = windows_path_maker(commends[1])
            if folder_path == None:
                return True
            text = Text_editor(name, folder_path, int(commends[2]))
            try:
                text.delete_line()
            except FileNotFoundError:
                print(f"\33[31m< {name} > file was not found.\33[0m")
            return True
#,,,,,cat,,,,,#
        case "cat":
            path_list = commends[1].split('/')
            if len(path_list) == 1:
                text = Text_reader(commends[1], windows_path)
                try:
                    text.read()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if cm == '$':
                folder_path = path_maker(commends[1])
            else:
                folder_path = windows_path_maker(commends[1])
            if folder_path == None:
                return True
            text = Text_reader(name, folder_path)
            try:
                text.read()
            except FileNotFoundError:
                print(f"\33[31m< {name} > file was not found.\33[0m")
            return True
#,,,,,mv,,,,,#
        case "mv":
            sc_path_list = commends[1].split('/')
            name_sc = sc_path_list.pop(-1)
            sc_path = '/'.join(sc_path_list)
            if cm == '$':
                folder_sc_path = path_maker(sc_path)
            else:
                folder_sc_path = windows_path_maker(sc_path)
            if folder_sc_path == None:
                return True
            now_path = folder_sc_path + '/' + name_sc
            dn_path_list = commends[2].split('/')
            name_dn = dn_path_list.pop(-1)
            dn_path = '/'.join(dn_path_list)
            if cm == '$':
                folder_dn_path = path_maker(dn_path)
            else:
                folder_dn_path = windows_path_maker(dn_path)
            if folder_dn_path == None:
                return True
            new_path = folder_dn_path + '/' + name_dn
            place = In_new_place(now_path, new_path)
            place.cut()
            return True
#,,,,,cp,,,,,#
        case "cp":
            sc_path_list = commends[1].split('/')
            name_sc = sc_path_list.pop(-1)
            sc_path = '/'.join(sc_path_list)
            if cm == '$':
                folder_sc_path = path_maker(sc_path)
            else:
                folder_sc_path = windows_path_maker(sc_path)
            if folder_sc_path == None:
                return True
            now_path = folder_sc_path + '/' + name_sc
            dn_path_list = commends[2].split('/')
            name_dn = dn_path_list.pop(-1)
            dn_path = '/'.join(dn_path_list)
            if cm == '$':
                folder_dn_path = path_maker(dn_path)
            else:
                folder_dn_path = windows_path_maker(dn_path)
            if folder_dn_path == None:
                return True
            new_path = folder_dn_path + '/' + name_dn
            place = In_new_place(now_path, new_path)
            place.copy()
            return True
#,,,,,rename,,,,,#
        case "rename":
            path_list = commends[1].split('/')
            if len(path_list) == 1 :
                name = Rename(commends[1], commends[2], windows_path)
                try:
                    name.rename()
                except FileNotFoundError:
                    print("\33[31mThe system can not find the folder path.\33[0m")
                except FileExistsError:
                    print("\33[31mAn object with this name already exists.\33[0m")
                return True
            old_name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if cm == '$':
                folder_path = path_maker(commends[1])
            else:
                folder_path = windows_path_maker(commends[1])
            if folder_path == None:
                return True
            name = Rename(old_name, commends[2], folder_path)
            try :
                name.rename()
            except FileNotFoundError :
                print("\33[31mThe system can not find the folder path.\33[0m")
            except FileExistsError :
                print("\33[31mAn object with this name already exists.\33[0m")
            return True
#,,,,,ls,,,,,#
        case "ls":
            files = os.listdir('.')
            if len(files) == 0 :
                print("(empty)")
                return True
            max = [0 , ""]
            for file in files :
                if len(file) > max[0] :
                    max[0] = len(file)
                    max[1] = file
            if max[1].count('.') != 1 :
                max[0] += 2
            print('|', '-' * (max[0] + 20), '|' , sep = '')
            for file in files :
                if file.count('.') == 1 :
                    print(f"|  {file}", " " * (max[0] - len(file) + 10), '(file)  |', sep = '')
                else :
                    print(f"|  {file}", " " * (max[0] - len(file) + 8), '(folder)  |', sep = '')
            print('|', '-' * (max[0] + 20), '|', sep = '')
            return True
        case "cm&pr" :
            return None
        case _ :
            return False

def know_management():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('INFORMATION PAGE')
    window.resize(1200, 600)

    window.resize(500, 1000)

    label_font1 = QFont("Arial", 18, QFont.Weight.Bold)
    label_font2 = QFont("Arial", 12, QFont.Weight.Bold)

    label1 = QLabel("COMMAND PREVIEW :")
    label1.setFont(label_font1)

    label2 = QLabel("< # > : To do things with Windows' own paths directly but based on Unix commands.")
    label2.setFont(label_font2)
    label2.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label3 = QLabel("< $ > : To do things with Unix.")
    label3.setFont(label_font2)
    label3.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label4 = QLabel("COMMAND : ")
    label4.setFont(label_font1)

    label5 = QLabel("To make folder : mkdir <path> <folder_name> or mkdir <folder_name>")
    label5.setFont(label_font2)
    label5.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label6 = QLabel("To make file : touch <path> <file_name>.txt or touch <file_name>.txt")
    label6.setFont(label_font2)
    label6.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label7 = QLabel("To delete folder or file : rm <path>")
    label7.setFont(label_font2)
    label7.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label8 = QLabel("To return to the previous folder : cd..")
    label8.setFont(label_font2)
    label8.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label9 = QLabel("To go to any folder : cd <path>")
    label9.setFont(label_font2)
    label9.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label10 = QLabel("To edit a file : nwfiletxt <path>")
    label10.setFont(label_font2)
    label10.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label11 = QLabel("To add new text to the file : appendtxt <path>")
    label11.setFont(label_font2)
    label11.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label12 = QLabel("To edit a specific line of the file : editline <path> <line> <text>")
    label12.setFont(label_font2)
    label12.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label13 = QLabel("To delete a specific line of the file : deline <path> <line>")
    label13.setFont(label_font2)
    label13.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label14 = QLabel("To view the file contents : cat <path>")
    label14.setFont(label_font2)
    label14.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label15 = QLabel("To view the contents of a folder that is inside : ls")
    label15.setFont(label_font2)
    label15.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label16 = QLabel("To copy a file or folder : cp <source_path> <destination_path>")
    label16.setFont(label_font2)
    label16.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label17 = QLabel("To move a file or folder : mv <source_path> <destination_path>")
    label17.setFont(label_font2)
    label17.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label18 = QLabel("To rename a file or folder : rename <path> <new_name>")
    label18.setFont(label_font2)
    label18.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    label19 = QLabel("To return to command preview : cm&pr")
    label19.setFont(label_font2)
    label19.setStyleSheet("""
        QLabel {
            color: #ffffff;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
        }
    """)

    layout = QVBoxLayout()
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)
    layout.addWidget(label4)
    layout.addWidget(label5)
    layout.addWidget(label6)
    layout.addWidget(label7)
    layout.addWidget(label8)
    layout.addWidget(label9)
    layout.addWidget(label10)
    layout.addWidget(label11)
    layout.addWidget(label12)
    layout.addWidget(label13)
    layout.addWidget(label14)
    layout.addWidget(label15)
    layout.addWidget(label16)
    layout.addWidget(label17)
    layout.addWidget(label18)
    layout.addWidget(label19)
    window.setLayout(layout)
    window.show()
    app.exec()
    return

#<<<<<<< Start managing the program >>>>>>>
command_list = ["mkdir", "rm", "touch", "cd..", "cd", "newfiletxt", "appendtxt",
                "editline", "deline", "cat", "mv", "cp", "rename", "ls"]
base_path = os.getcwd()
base_path_list = base_path.split('\\')
base_path = '/'.join(base_path_list)
unix_path = "//"
windows_path = base_path
count = 1
start_detail = """\33[35mwelcome !
To know how to use this terminal, type the word 'know'.
for start this terminal, type the word 'start'.\33[0m"""
print(start_detail)
#,,,,,start_panel,,,,,#
while True :
    choice = input("your choice : ")
    if choice == "know" :
        know_management()
        continue
    elif choice == "start" :
        break
    else :
        print("\33[31mThe input is invalid; try again.\33[0m")
        continue
#,,,,,terminal_panel,,,,,#
while True :
    try :
        cm = input("Enter your command preview : ")
        if cm == '$' :
            if base_path in windows_path :
                os.chdir(windows_path)
            else :
                os.chdir(base_path)
            while True :
                print(f"\33[4m\33[34mTerminal~Comm&Line:{count}\33[0m\33[33m -> {unix_path} $ \33[0m", end="")
                recipient = input()
                Commands = recipient.split()
                result = Linked_function(Commands)
                if result == False :
                    print("\33[31mThis commander was not found.\33[0m")
                    count += 1
                    continue
                elif result == None :
                    break
                count += 1
                continue
            count += 1
            continue
        elif cm == '#' :
            os.chdir(windows_path)
            while True :
                print(f"\33[4m\33[34mTerminal~Comm&Line:{count}\33[0m\33[33m -> {windows_path} # \33[0m", end="")
                recipient = input()
                Commands = recipient.split()
                result = Linked_function(Commands)
                if result == False :
                    print("\33[31mThis commander was not found.\33[0m")
                    count += 1
                    continue
                if result == None :
                    break
                count += 1
                continue
            count += 1
            continue
        else:
            print("\33[31mThis commander preview was not found.\33[0m")
            count += 1
            continue
        count += 1
    except IndexError :
        print("\33[31mThe enter items are not correct.\33[0m")
        count += 1
        continue
    except EOFError :
        print("End !")
        break


