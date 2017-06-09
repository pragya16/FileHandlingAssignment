
# Question 16 : Write a Python program to remove newline characters from a file

def remove_newline(fname):  

    list = open(fname).readlines()  
    return [s.rstrip('\n') for s in list]  
  
print(remove_newline("test.txt"))  

'''
output:
[root@demo FileHandlingAssignment]# python program16.py
['What is Python language?    ',
'2 2 Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.         ', 
'3 3 Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in   ', 
'4 4 languages such as C++ or Java.                                           ',
'5 5 Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles.            ', 
'6 6 It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.                             ', '7 7 The best way we learn anything is by practice and exercise questions. We  have started this section for those (beginner to intermediate) who are   ', '8 8 familiar with Python.  ']
'''
