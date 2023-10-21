# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     cioy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('31_test.txt', '32_copy.txt')  # src, dst
