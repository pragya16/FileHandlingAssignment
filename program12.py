
# Question 12 : Write a Python program to copy the contents of a file to another file

from shutil import copyfile

import os

os.system("touch abc.txt ")
copyfile('text.txt', 'abc.txt')


'''
output:

'''
