fhand = open('foo.txt','r')

#read all the content at on
fcontent = fhand.read()

print(fcontent)

#read lines into a list of lines
fhand = open('foo.txt','r')
fcontent2 = fhand.readlines()

print(fcontent2)

#read line by looping

fhand = open('foo.txt','r')

fcontent3 = fhand.readlines()

for line in fcontent3:
	line = line.rstrip()
	print(line)