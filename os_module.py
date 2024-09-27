import os
import shutil


# GETTING THE CURRENT PATH
local_ = os.getcwd()

# CREATING A PATH TO OUR DIRECTORY
FOLDER_TEST_OS_LIB = os.path.join(local_, 'FOLDER_TEST_OS_LIB')

# MAKING A DIRECTORY
if not os.path.exists(FOLDER_TEST_OS_LIB):
    os.mkdir(FOLDER_TEST_OS_LIB)

# CREATING A FILE INTO THE OUR FOLDER
FILE_PATH = os.path.join(FOLDER_TEST_OS_LIB, 'test_os_lib.txt')

with open(FILE_PATH, 'w', encoding='UTF8') as file:
    file.write('Hi! This file is a test about what i learned on my classes \
os module. ')
    file.close()

# MOVING A FILE INTO THE OUR FOLDER
shutil.move(os.path.join(local_, 'test_os_lib_2.txt'), FOLDER_TEST_OS_LIB)