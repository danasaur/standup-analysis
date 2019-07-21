import os
import errno

# Taken from https://stackoverflow.com/a/600612/119527
def mkdir_p(path):
    """ add the necessary directories for this path 
    if they don't exist yet. pass if they do"""
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        pass

def main():
    print("hello world: executed function!")
    path = os.getcwd()
    file_name = "test2.txt"
    file_directory = "{0}/{1}/".format(path, "transcripts")
    file_path = "{0}{1}".format(file_directory, file_name)
    
    mkdir_p(file_directory)

    with open(file_path, "w") as file_name:
        file_name.write("hello world: wrote to a file!")

if __name__ == '__main__':
    main()
