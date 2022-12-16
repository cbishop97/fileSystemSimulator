"""
Chance's File System Simulator
Supported commands are 'mkdir', 'cd', 'touch', and 'ls'
Type 'quit' to end program

The files and folders that are created in this program will only exist in memory.
They will not be created within your systems disk space.
This program can not interact with folders and files in your systems disk space.
After the program is ended the files and folders created during run time will be lost.

"""
class Directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.directories = []
        self.files = []
        self.parent = parent

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.currDir = self.root

    def mkdir(self, dirName):
        for i in self.currDir.directories:
            if i.name == dirName:
                print(f"Directory named '{dirName}' already exists")
                return
        self.newDir = Directory(dirName, self.currDir)
        self.currDir.directories.append(self.newDir)

    def ls(self):
        for i in self.currDir.directories:
            print(i.name)
        for i in self.currDir.files:
            print(i)

    def touch(self, fileName):
        for i in range( len(self.currDir.files) ):
            if self.currDir.files[i] == fileName + ".txt":
                print(f"File named '{fileName}.txt' already exists")
                return
        self.currDir.files.append(fileName + ".txt")

    def cd(self, dirName):
        if dirName == "..":
            if self.currDir == self.root:
                return
            self.currDir = self.currDir.parent
            return
        if dirName == "/":
            self.currDir = self.root
            return

        self.find_path(dirName)

    def find_path(self, path):
        checkRoot = path[0:1]
        origDir = self.currDir
        path = path.split("/")
        if checkRoot == "/":
            path.pop(0)
            self.currDir = self.root

        for dName in path:
            found = False
            for d in self.currDir.directories:
                if d.name == dName:
                    self.currDir = d
                    found = True

            if found == False:
                self.currDir = origDir
                print(f"Directory named '{dName}' does not exist")
                return

#Error handling functions
def input_error(cmd = None):
    if cmd == "cd":
        print("The 'cd' command needs a directory name or use '..' to go to the previous directory")
        return
    print("Sorry, this program only supports up to two inputs")
    print("Try entering 'mkdir folder_name' or 'touch file_name', 'cd', or 'ls'.")

def name_needed_error(cmd):
    if cmd == "mkdir":
        print("A directory name is needed for this command")
    elif cmd == "touch":
        print("A file name is needed for this command")
    else:
        print("Something went wrong")

def general_error():
    print("***Something went wrong")
    print("This program only supports the commands 'mkdir', 'touch', 'cd', and 'ls'")

#Main function begins
fs = FileSystem()
while True:

    userInput = input(f"[chance@fileSystem {fs.currDir.name} ] $ ")
    userInput = userInput.split()

    if len(userInput) > 2:
        input_error()

    elif len(userInput) == 0:
        continue

    elif userInput[0] == "mkdir":
        if len(userInput) == 1:
            name_needed_error(userInput[0])
        elif "/" in userInput[1]:
            print("The '/' character can not be used in the directory name")
        else:
            fs.mkdir(userInput[1])

    elif userInput[0] == "touch":
        if len(userInput) == 1:
            name_needed_error(userInput[0])
        else:
            fs.touch(userInput[1])

    elif userInput[0] == "cd":
        if len(userInput) < 2:
            input_error(userInput[0])
        else:
            fs.cd(userInput[1])

    elif userInput[0] == "ls":
        fs.ls()

    elif userInput[0] == "quit":
        break

    else:
        general_error()