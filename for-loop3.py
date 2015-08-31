number_list = [3, 41, 12, 9, 74, 15,95,2,156,1]
largest = None
print("The largest before: ",largest)
for number in number_list:
	if largest is None or number > largest:
		largest = number
		print("Current largest: ",largest)
print("largest: ",largest)

