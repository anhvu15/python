def compute_pay(hours,rate):
	payment = 0.0
	if hours <= 40:
		payment = hours*rate
	else:
		payment = (40*rate) + (hours-40)*rate*1.5
	return payment

def get_input(prompt):
	passed = False
	number = 0.0
	while not passed:
		try:
			number = float(input(prompt))
			passed = True	
		except:
			print('Invalid Number!')
	return number
answer = 'Y'
while answer.upper() == 'Y':
	hours = get_input('Enter Hours: ')
	rate = get_input('Enter Rate: ')
	payment = compute_pay(hours,rate)
	print('Pay: ',payment)
	answer = input("Do you want to continue(Y/N): ")
	

print('Bye')