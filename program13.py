
# Question 13 : Write a Python program to copy the contents of a file to another file

with open('abc.txt') as f1, open('test.txt') as f2:  
    for l1, l2 in zip(f1, f2):  
        # l1 from abc.txt, l2 from test.txt 
        print(l1+l2)  

'''
output:
[root@demo FileHandlingAssignment]# python program13.py
apple
What is Python language?                                                 
mango2
2 Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.                                                  
banana3 
3 Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in   
watermelon4 
4 languages such as C++ or Java.                                          
papaya5
5 Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles.            
lichi6 
6 It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.                             
'''

