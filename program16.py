# Question 16 : Write a Python program to remove newline characters from a file

def remove_newline(fname):  

    list = open(fname).readlines()  
    return [s.rstrip('\n') for s in list]  
  
print(remove_newline("test.txt"))  

'''
output:
'''
