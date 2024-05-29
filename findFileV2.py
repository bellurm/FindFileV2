# Used Composite Pattern

import os
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def search(self, name):
        pass

class File(FileSystemComponent):
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    def search(self, name):
        if self.name == name:
            print(f"[FOUND] '{name}' is here: {self.path}")
            return True
        return False

class Directory(FileSystemComponent):
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    def search(self, name):
        try:
            for dirpath, dirnames, filenames in os.walk(self.path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    file_component = File(file_path)
                    if file_component.search(name):
                        return True
        except PermissionError:
            print(f"[WARNING] Permission denied: {self.path}")
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")
        return False

if __name__ == "__main__":
    path = input("Where are you looking for the file? [eg: C:/, D:/, /root, /kali etc.] > ")
    get_file = input("What is the file name? > ")

    if os.path.isdir(path):
        root_directory = Directory(path)
        if not root_directory.search(get_file):
            print(f"[NOT FOUND] '{get_file}' is not found in {path}.")
    else:
        print(f"[NOT FOUND] The path '{path}' is not a directory. Please enter a valid directory path.")
