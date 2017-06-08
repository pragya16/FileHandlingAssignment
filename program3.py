# Question 3:Write a Python program to append text to a file and display the text


def file_read(fname):  
        from itertools import islice  
        with open(fname, "a+") as t1:  
                t1.write("Python Exercises is good for learning python\n")  
                t1.write("Java Exercises is good for increase knowldge")  
        txt = open(fname)  
        print(txt.read())  
print file_read('test.txt')  

'''
output:
[root@demo FileHandlingAssignment]# python program3.py

'''
