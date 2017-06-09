# Question 8:Write a python program to find the longest words


text= "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language"
longest = 0
for word in text.split():
    if len(word) > longest:
        longest = len(word)
    longest_word = word
print( "The longest word is %s" % longest_word )


'''
output:

'''

