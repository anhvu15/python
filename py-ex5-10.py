def get_number():
	user_input = None
	total = 0.0	
	while True:
		try:
			user_input = input("Enter a number:  ")
			if user_input.upper() != "DONE":
				number = float(user_input)
				total += number
			else:
				break
		except:
			print("Invalid number")
	return total

print("Total ",get_number())