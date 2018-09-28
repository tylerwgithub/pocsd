import MemoryInterface, AbsolutePathNameLayer

def Initialize_My_FileSystem():
    MemoryInterface.Initialize_My_FileSystem()
    AbsolutePathNameLayer.AbsolutePathNameLayer().new_entry('/', 1)

#HANDLE TO ABSOLUTE PATH NAME LAYER
interface = AbsolutePathNameLayer.AbsolutePathNameLayer()

class FileSystemOperations():

    #MAKES NEW DIRECTORY
    def mkdir(self, path):
        interface.new_entry(path, 1)

    #CREATE FILE
    def create(self, path):
        interface.new_entry(path, 0)
        

    #WRITE TO FILE
    def write(self, path, data, offset=0):
        interface.write(path, offset, data)
      

    #READ
    def read(self, path, offset=0, size=-1):
        read_buffer = interface.read(path, offset, size)
        if read_buffer != -1: print(path + " : " + read_buffer)

    
    #DELETE
    def rm(self, path):
        interface.unlink(path)


    #MOVING FILE
    def mv(self, old_path, new_path):
        interface.mv(old_path, new_path)

    def link(self, old_path, new_path):
        interface.link(old_path, new_path)
        
    #CHECK STATUS
    def status(self):
        print(MemoryInterface.status())
        
    def print_files_and_inodes(self, path):
        interface.print_files_and_inodes(path)



if __name__ == '__main__':
    #DO NOT MODIFY THIS
    Initialize_My_FileSystem()
    my_object = FileSystemOperations()
    #my_object.status()
    #YOU MAY WRITE YOUR CODE AFTER HERE

    my_object.mkdir("/A")
    #my_object.mkdir("/B")
#    my_object.status()
    my_object.create("/A/1.txt")
    my_object.mkdir("/A/B")
    my_object.mkdir("/A/B/C")
    my_object.create("/A/B/C/1.txt")
    my_object.write("/A/1.txt", "test data", 0)
    my_object.link("/A/1.txt", "/A/B/C/2.txt")
    my_object.rm("/A/1.txt")
    my_object.mv("/A/B/C/2.txt", "/A/B/3.txt")
    my_object.rm("/A/B/C/1.txt")
    my_object.rm("/A/B/C")
    my_object.status()
    
    '''Examples:
    my_object.mkdir("/A")
    my_object.status()
    my_object.mkdir("/B")
    my_object.status()
    my_object.create("/A/1.txt"), as A is already there we can crete file in A
    my_object.status()
    my_object.write("A/1.txt", "POCSD", offset), as 1.txt is already created now, we can write to it.
    my_object.status()
    my_object.mv("/A/1.txt", "/B")
    my_object.status()
    my_object.rm("A/1.txt")
    my_object.status()
    '''

