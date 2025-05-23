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
        path = unix_path[2:1]
    path_list =base_path.split("\\")
    correct_path = "/".join(path_list)
    new_path = correct_path + "/" + path
    now_path = os.getcwd()
    try :
        os.chdir(new_path)
    except FileNotFoundError :
        print("\33[31mThe given path was not found.\33[0m")
        return None
    os.chdir(now_path)
    return new_path

def Linked_function(commends : list) :
    global unix_path
    global base_path
    match commends[0] :
#,,,,,mkdir,,,,,#
        case "mkdir" :
            if len(commends) == 2 :
                folder_path = path_maker(unix_path)
                if folder_path == None :
                    return True
                name = commends[1]
                folder = Folder_maker(folder_path, name)
                folder.make_folder()
            elif len(commends) == 3 :
                folder_path = path_maker(commends[1])
                if folder_path == None :
                    return True
                name = commends[2]
                folder = Folder_maker(folder_path, name)
                folder.make_folder()
            return True
#,,,,,rm,,,,,#
        case "rm":
            path_list = commends[1].split('/')
            if len(path_list) == 1 :
                if commends[1][-4:] == ".txt":
                    file = File_deleter(os.getcwd(), commends[1])
                    try :
                        file.delete_file()
                    except FileNotFoundError :
                        print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                    return True
                else:
                    folder = Folder_deleter(os.getcwd(), commends[1])
                    try:
                        folder.delete_folder()
                    except OSError:
                        print(f"\33[31m< {commends[1]} > directory is not empty.\33[0m")
                    return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            if name[-4:] == ".txt" :
                folder_path = path_maker(commends[1])
                if folder_path == None :
                    return True
                file = File_deleter(folder_path, name)
                try:
                    file.delete_file()
                except FileNotFoundError:
                    print(f"\33[31m< {name} > file was not found.\33[0m")
                    return True
            else :
                folder_path = path_maker(commends[1])
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
                folder_path = path_maker(unix_path)
                if folder_path == None :
                    return True
                name = commends[1]
                file = File_maker(folder_path, name)
                file.make_file()
            elif len(commends) == 3 :
                folder_path = path_maker(commends[1])
                if folder_path == None :
                    return True
                name = commends[2]
                file = File_maker(folder_path, name)
                file.make_file()
            return True
#,,,,,cd..,,,,,#
        case "cd..":
            if unix_path == "//" :
                return True
            unix_folder_path = unix_path[2:-1]
            unix_path_list = unix_folder_path.split('/')
            unix_path_list.pop(-1)
            if len(unix_path_list) == 0 :
                unix_path = "//"
            else :
                unix_path = "//" + '/'.join(unix_path_list) + '/'
            folder_path_list = os.getcwd().split('\\')
            folder_path_list.pop(-1)
            folder_path = '/'.join(folder_path_list)
            moving = Navigation(folder_path)
            moving.movement()
            return True
#,,,,,cd,,,,,#
        case "cd":
            folder_path = path_maker(commends[1])
            if folder_path == None:
                return True
            unix_path = "//" + commends[1] + "/"
            moving = Navigation(folder_path)
            moving.movement()
            return True
#,,,,,newfiletxt,,,,,#
        case "newfiletxt":
            path_list = commends[1].split('/')
            if len(path_list) == 1 :
                file = File_editor(os.getcwd(), commends[1])
                file.newfile()
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            folder_path = path_maker(commends[1])
            if folder_path == None:
                return True
            file = File_editor(folder_path, name)
            file.newfile()
            return True
#,,,,,appendtxt,,,,,#
        case "appendtxt":
            path_list = commends[1].split('/')
            if len(path_list) == 1:
                file = File_editor(os.getcwd(), commends[1])
                try :
                    file.append()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            folder_path = path_maker(commends[1])
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
                text = Text_editor(commends[1], os.getcwd(), int(commends[2]), commends[3])
                try:
                    text.edit_line()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            folder_path = path_maker(commends[1])
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
                text = Text_editor(commends[1], os.getcwd(), int(commends[2]))
                try:
                    text.delete_line()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            folder_path = path_maker(commends[1])
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
                text = Text_reader(commends[1], os.getcwd())
                try:
                    text.read()
                except FileNotFoundError:
                    print(f"\33[31m< {commends[1]} > file was not found.\33[0m")
                return True
            name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            folder_path = path_maker(commends[1])
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
            folder_sc_path = path_maker(sc_path)
            if folder_sc_path == None:
                return True
            now_path = folder_sc_path + '/' + name_sc
            dn_path_list = commends[2].split('/')
            name_dn = dn_path_list.pop(-1)
            dn_path = '/'.join(dn_path_list)
            folder_dn_path = path_maker(dn_path)
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
            folder_sc_path = path_maker(sc_path)
            if folder_sc_path == None:
                return True
            now_path = folder_sc_path + '/' + name_sc
            dn_path_list = commends[2].split('/')
            name_dn = dn_path_list.pop(-1)
            dn_path = '/'.join(dn_path_list)
            folder_dn_path = path_maker(dn_path)
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
                name = Rename(commends[1], commends[2], base_path)
                try:
                    name.rename()
                except FileNotFoundError:
                    print("\33[31mThe system can not find the folder path.\33[0m")
                except FileExistsError:
                    print("\33[31mAn object with this name already exists.\33[0m")
                return True
            old_name = path_list.pop(-1)
            commends[1] = '/'.join(path_list)
            folder_path = path_maker(commends[1])
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
            print('|', '-' * 48, '|')
            for file in files :
                if '.' in file :
                    print(f"|  {file}", " " * (38 - len(file)), '(file)  |')
                else :
                    print(f"|  {file}", " " * (36 - len(file)), '(folder)  |')
            print('|', '-' * 48, '|')
            return True
        case _ :
            return False
