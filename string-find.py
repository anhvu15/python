data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
start = data.find('@')
end = data.find(' ',start)
print(data[start+1:end])