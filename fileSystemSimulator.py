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
        self.parent = parent
        self.files = []
        self.directories = []

    def mkdir(self, dirName):
        #check if directory name already exists in derectories array
        for d in self.directories:
            if d.name == dirName:
                print("Directory with that name already exists")
                return
        #if directory name doesn't exist create new directory instance and add it to directories array
        newDir = Directory(dirName, self)
        self.directories.append(newDir)

    def ls(self):
        #prints names of directories in directories array
        for d in self.directories:
            print(d.name)
        #prints names of files in files array
        for f in self.files:
            print(f)

    def touch(self, fileName):
        #loop through files array and check if file name already exists
        for f in self.files:
            if f.name == fileName:
                print("File with with that name already exists")
                return
        #if file name does not exist add file name to files array
        self.files.append(fileName + ".txt")

    def cd(self, dirName):
        #check if dirName is in directories array, if found return directory
        for d in self.directories:
            if d.name == dirName:
                return d
        #if final directory in path is not found this will print and false will be returned
        print("No directory with that name exists")
        return False


class FileSystem:
    def __init__(self):
        #create instance of directory class with name '/'
        self.root = Directory("/")
        #assign root directory as current directory
        self.currDir = self.root

    def mkdir(self, dirName):
        self.currDir.mkdir(dirName)

    def ls(self):
        self.currDir.ls()

    def touch(self, fileName):
        self.currDir.touch(fileName)

    def cd(self, dirName):
        #if user enters '..' as cd argument
        if dirName == "..":
            #if current directory is root return
            if self.currDir.name == "/":
                return
            #if current directory is not root set parent directory as current directory
            self.currDir = self.currDir.parent
            return
        #if user enters '/' as cd argument set root as current directory
        if dirName == "/":
            self.currDir = self.root
            return
        #split users input using
        path = dirName.split("/")
        #holds original directory
        temp = self.currDir
        #for # of splits in path call cd function in directory class
        for dName in path:
            self.currDir = self.currDir.cd(dName)
            #if directory in path is not found set current directory back to original directory and break loop
            if not self.currDir:
                self.currDir = temp
                break


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
    userInput = input("[chance@fileSystem {} ] $ ".format(fs.currDir.name))
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