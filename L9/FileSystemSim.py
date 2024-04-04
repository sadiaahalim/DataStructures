class FileEntry:
    def __init__(self, name, parent):
        self.type = '-'
        self.name = name
        self.parent = parent

    def __str__(self):
        return "File: " + str(self.name)


class FolderEntry:
    def __init__(self, name, parent):
        self.type = 'd'
        self.name = name
        self.children = []
        self.parent = parent
    def __str__(self):
        return "Folder: " + str(self.name)


class FileSystem:
    # Initialize the file system.  Create a root directory and make the current directory
    # the root.
    def __init__(self):
        self.root = FolderEntry("/",None)
        self.root.parent = self.root
        self.current_dir = self.root
        

    # Change to the given directory.  To make this as simple as possible you only need
    # to support a single directory change relative to the current working directory
    # this includes the parent (..) folder.
    #
    # If the path doesn't exist just print an error message but do not do anything.
    def cd(self, path):

        for p in self.current_dir.children:

            if p.type == "d" and p.name == path:
                    self.current_dir = p
        if path == "..":
                self.current_dir = self.current_dir.parent

    # Create a file with the given name in the current working directory.  If a file already exists
    # this function should print an error and ignore the operation
    def touch(self, fname):
        for z in self.current_dir.children:
            if z.name == fname:
                print("File already Exists")
                return

        file = FileEntry(fname,self.current_dir)
        file.parent = self.current_dir
        self.current_dir.children.append(file)
        

    # Create a folder in the current working directory.
    def mkdir(self, dname):
        for z in self.current_dir.children:
            if z.name == dname:
                raise Exception("Folder already Exists")
        folder = FolderEntry(dname,self.current_dir)
        if self.current_dir.type == "d":
            self.current_dir.children.append(folder)
       
            

    # Display a listing of the file/folders in the current working directory
    def ls(self):
        for x in self.current_dir.children:
            print(x)
                
                

    def tree_recursive(self,root):
        for child in root.children:
            if child.type == "d":
                myword = ""
                if len(child.children) == 0:
                    myword += child.name + "/"
                    temp_folder = child
                    while temp_folder.parent.name != self.current_dir.name:
                        myword += temp_folder.parent.name + "/"
                        temp_folder = temp_folder.parent
                    temp = myword.split("/")
                    temp.reverse()
                    temp_myword = ""
                    for i in temp:
                        if i != "":
                            temp_myword += i + "/"
                    print(temp_myword[0:-1])
                else:
                    self.tree_recursive(child)
                
            if child.type == "-":
                myword = ""
                myword += child.name + "/"
                temp_folder = child
                while temp_folder.parent.name != self.current_dir.name:
                    myword += temp_folder.parent.name + "/"
                    temp_folder = temp_folder.parent
                temp = myword.split("/")
                temp.reverse()
                temp_myword = ""
                for i in temp:
                    if i != "":
                        temp_myword += i + "/"
                print(temp_myword[0:-1]) 

        
    
                
    # Print a list of everything in the file system starting with the current working directory.  Hint:
    # This is just like a preorder traversal.  When printing the name of the file print the full
    # path to the file starting with the root directory and include the / symbol between each folder name.

    def tree(self):
        print(self.root)
        self.tree_recursive(self.current_dir)


        
    def find_recursive(self, root, name):
        for child in root.children:
            if child.type == "-":
                myword = ""
                if child.name == name:
                    myword += child.name + "/"
                    temp_folder = child
                    while temp_folder.parent.name != self.current_dir.name:
                        myword += temp_folder.parent.name + "/"
                        temp_folder = temp_folder.parent
                    temp = myword.split("/")
                    temp.reverse()
                    temp_myword = ""
                    for i in temp:
                        if i != "":
                            temp_myword += i + "/"
                    print(temp_myword[0:-1])
            else:
                self.find_recursive(child, name)

                
    # Find all the files and folders in the file system starting with the current folder that match the given name.
    # The function will return a list of strings in the full path format.
    def find(self, name):
        self.find_recursive(self.current_dir, name)



drive = FileSystem()
drive.mkdir("usr")
drive.mkdir("etc")
drive.mkdir("home")
drive.cd("home")
drive.touch("asas.txt")
drive.mkdir("student")
drive.cd("student")
drive.touch("student.conf")
drive.mkdir("public_html")
drive.touch("rakif.html")
drive.cd("..")
drive.cd("..")
drive.cd("etc")
drive.touch("student.conf")
drive.cd("..")

drive.tree()
print("====")
print(drive.find("student.conf"))

