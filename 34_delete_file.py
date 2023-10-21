import os
import shutil

# path = '34_test.txt'
text = "Yoooooooo\nI'm gonna be deleted soon\n"
path = '34'  # DIR

# with open(path, 'w') as file:
#     file.write(text)

try:
    os.remove(path)
    # os.rmdir(path)  # DIR
    # shutil.rmtree(path) # not empty dir, dangerous
except FileNotFoundError:
    print('File 404')
except PermissionError:
    print('You do not have persmission to delete that')
except OSError:
    print("You can't delete that using that function")
else:
    print(path + ' was deleted')
