file_path = 'C:\\temp\\sample.txt'
file = open(file_path,"w")
file.write('This is a writing text file demo.')
file.write('you can add end-of-line character\n So this is a new line\n')
file.write(""" Another way to make a new line
               in Python by using triple quotes""")
 
file.close()

