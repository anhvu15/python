# characters count
def characters_count(filename):
	fhand = open(filename)
	return len(fhand.read())

# words count
def words_count(filename):
	fhand = open(filename)
	return len(fhand.read().split())

#lines count

def lines_count(filename):
	fhand = open(filename)
	return len(fhand.readlines())

#count number of characters of foo.txt
print("Characters: ",characters_count('foo.txt'))

#count number of words of foo.txt
print("Words: ",words_count('foo.txt'))

#count number of lines of foo
print("Lines: ",lines_count('foo.txt'))


