
# Question 14 : Write a Python program to read a random line from a file

import random
str = open("text.txt").read().splitlines()
print random.choice(str)


'''
output:
output:
[root@demo FileHandlingAssignment]# python program14.py
apple
'''
