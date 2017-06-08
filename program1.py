 # Question 1: Write a Python program to read an entire text file and print its contents


# Open a file
fo1 = open("sample.txt", "r+")
print fo1.read()
print "Name of the file: ", fo1.name
print "Opening mode : ", fo1.mode
print "Softspace flag : ", fo1.softspace
print "Closed or not : ", fo1.closed

'''
output:

'''
