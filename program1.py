# Open a file
fo1 = open("zensar.txt", "w+")
fo1.write( "Python is a great language.\Now a days i am learning it.\it is intresting scripting language.\nYeah its great!!\n");
fo1.seek(0,0)
print fo1.read()
print "Name of the file: ", fo1.name
print "Opening mode : ", fo1.mode
print "Softspace flag : ", fo1.softspace
print "Closed or not : ", fo1.closed

'''
output:

'''
