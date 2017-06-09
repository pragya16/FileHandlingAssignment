# Question 13 : Write a Python program to copy the contents of a file to another file

with open('abc.txt') as fh1, open('test.txt') as fh2:  
    for l1, l2 in zip(f1, f2):  
        # l1 from abc.txt, l2 from test.txt 
        print(l1+l2)  

'''
output:
'''

