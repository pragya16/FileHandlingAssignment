# Question 4: Write a Python program to read last n lines of a file and display the same

def file_read(fname, nlines):  
        from itertools import islice  
        with open(fname) as f:  
                for line in islice(f, nlines):  
                        print(line)  
file_read('test.txt',-4)  


'''
output:

'''
