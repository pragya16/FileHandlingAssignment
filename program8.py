# Question 8:Write a python program to find the longest words


def Word():
    text= "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language"
    long = ''
for word in text.split():
    if len(word) > long:
       long = len(word)
       longest_word_here = word
print( "The longest word is %s" % longest_word_here)


'''
output:

'''

