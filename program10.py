
# Question 10 : Write a Python program to get the file size of a plain file

import os
str = os.stat('pc.txt')
print str.st_size

'''
output:
'''
