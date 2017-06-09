# Question 11 :Write a Python program to write a list to a file


fruit = ['apple', 'mango', 'banana', 'watermelon', 'papaya', 'lichi']  
with open('text.txt', "w") as file:  
        for f in fruit:  
                file.write("%s\n" % f)  
  
content = open('text.txt')  
print(content.read())  



'''
output:

'''
