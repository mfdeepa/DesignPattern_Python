from abc import ABC, abstractmethod


# Component Interface
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass


# Leaf Class
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self, indent=0):
        print(" " * indent + f"File: {self.name} (Size: {self.size} KB)")


# Composite Class
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show_details(indent + 4)


# Client Code
if __name__ == "__main__":
    # Leaf nodes
    file1 = File("file1.txt", 10)
    file2 = File("file2.txt", 20)
    file3 = File("file3.txt", 30)

    # Composite nodes
    folder1 = Folder("Documents")
    folder2 = Folder("Pictures")

    # Building the hierarchy
    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)

    root_folder = Folder("Root")
    root_folder.add(folder1)
    root_folder.add(folder2)

    # Displaying the hierarchy
    print("File System Structure:")
    root_folder.show_details()
