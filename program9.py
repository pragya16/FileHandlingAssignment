
# Question 9 :  Write a Python program to count the frequency of words in a file

file=open("text.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for a in wordcount.items():
    print a
    
'''
output:
[root@demo FileHandlingAssignment]# python program9.py('What', 1)('code', 2)('dynamic', 2)('syntax', 1)('including', 1)('its', 1)('readability,', 1)('languages', 1)('to', 2)('4', 2)('questions.', 1)('has', 1)('familiar', 1)('practice', 1)('emphasizes', 1)('language?', 1)('high-level,', 1)('language.', 1)('fewer', 1)('large', 1)('styles.', 1)('automatic', 1)('design', 1)('are', 1)('best', 1)('Python.', 1)('for', 1)('section', 1)('3', 2)('imperative', 1)('7', 2)('supports', 1)
('exercise', 1)('general-purpose,', 1)('we', 1)('philosophy', 1)('concepts', 1)('We', 1)('standard', 1)('by', 1)('anything', 1)('of', 1)('allows', 1)('Its', 1)('or', 2)('features', 1)('functional', 1)('paradigms,', 1)('management', 1)('interpreted,', 1)('system', 1)('2', 2)('way', 1)('6', 2)('type', 1)('object-oriented,', 1)('started', 1)('memory', 1)('8', 2)('intermediate)', 1)('with', 1)('than', 1)('those', 1)('this', 1)('express', 1)('learn', 1)('procedural', 1)('and', 6)('programming', 3)('is', 3)('as', 1)('have', 1)('in', 2)('Python', 3)('Java.', 1)('5', 2)('widely', 1)('used', 1)('multiple', 1)('programmers', 1)('comprehensive', 1)('who', 1)('C++', 1)('possible', 1)('such', 1)('The', 1)('a', 3)('lines', 1)('It', 1)('(beginner', 1)('library.', 1)

'''
