# Question 7 : Write a Python program to read a file line by line store it into an array

f_array = []
with open(''test.txt'',"r") as file:
    for lines in file:
        f_array.append(lines)
    print(f_array)

'''
output:

'''
