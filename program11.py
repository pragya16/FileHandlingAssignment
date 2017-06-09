# Question 11 :Write a Python program to write a list to a file

file=open("text.txt","w+")
for item in file:
  file.write("%s\n" % item)
print >> file , item

'''
output:

'''
