
# Question 12 : Write a Python program to copy the contents of a file to another file

from shutil import copyfile

str = copyfile('text.txt', 'abc.txt')
str.seek(0,0)
print read('abc.txt')

'''
output:

'''
