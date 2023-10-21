import os

path = "C:\\Users\\user\\projets\\python\\helloWorld\\test.txt"
folder_path = "C:\\Users\\user\\projets\\python\\helloWorld"
# same directory ? file_name : file_path

test_path = folder_path

if os.path.exists(test_path):
    print("That location exists")
    if os.path.isfile(test_path):
        print('That is a file')
    elif os.path.isdir(test_path):
        print('That is a directory')
else:
    print('Error 404')
