def my_zip(a,b):
	return [(a[x],b[y]) for x in range(len(a)) for y in range(len(b)) if x==y ]


a = zip([1, 2, 3,4], ["a", "b", "c"])
for x,y in a:
	print(x,y)
print(my_zip([1, 2, 3,4], ["a", "b", "c"]))