# Question 8:Write a python program to find the longest words


def Word():
    f= "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language"
    long=''
    for l in f:
        if len(l)>len(long):
            long=l
    return long
print Word()


'''
output:

'''

