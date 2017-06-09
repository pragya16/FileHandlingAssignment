
# Question 15 : Write a Python program to assess if a file is closed or not


f=open("text.txt","r")
f1=open("test.txt","r")
print(f.closed)
f.close()
print(f1.closed)
f1.close()
print(f.closed)
print(f1.closed)

'''
output:

'''
