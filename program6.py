
# Question 6 :Write a Python program to read a file line by line store it into a variable

with open ("test.txt", "r") as file:
    str=file.readlines()
    print(str)
    
    
    '''
    output:
    [root@demo FileHandlingAssignment]# python program6.py
    ['Python Exercises is good for learning python\n', 
    'Java Exercises is good for increase knowldgePython Exercises is good for learning python\n',
    'Java Exercises is good for increase knowldgePython Exercises is good for learning python\n', 
    'Java Exercises is good for increase knowldge']
    '''
