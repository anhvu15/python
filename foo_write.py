# fhand = open('foo_write.txt','w')

# fhand.write("a\nb\nc\n")

# fhand.close()

fhand = open('foo_write.txt','w')

fhand.writelines(['hello\n','good morning\n','good evening\n'])

fhand.close()