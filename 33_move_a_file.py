import os
import shutil

# source = "33_file_to_move.txt"
source = "33_folder_to_move"
# destination = "C:\\Users\\user\\projets\\python\\helloWorld\\33\\" + source
destination = "C:\\Users\\user\\projets\\python\\helloWorld\\33\\" + source

shutil.copy('32_copy.txt', source)  # src, dst

try:
    if os.path.exists(destination) & os.path.isfile(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source + " was moved to " + destination)
except FileNotFoundError:
    print(source + " was not found")
