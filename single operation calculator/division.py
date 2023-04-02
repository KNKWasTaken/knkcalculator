#Importing sys
import sys

#Functions
def invalid_exit():
	invexit = input('Do You Want To Exit? (y/n)')
	if invexit.lower() == 'y':
		print('Exiting...')
		sys.exit(0)
	elif invexit.lower() == 'n':
		print('Continuing With Calculation...')
	else:
		print('Invalid Data. Continuing With Calculation...')
		
divide_list = lambda list: 0 if len(list) == 0 else (list[0] if len(list) == 1 else list[0] / divide_list(list[1:]))

#Telling User How to Exit and Get Results
print('Enter E to Exit')
print('Enter R for Results')

#Predefined Values
l = list() #Creates Empty list

while True:
	v = input(f'Enter Number {len(l) + 1}: ')
	if v.isnumeric():
		l.append(int(v))
	elif v.lower() == 'r':
		if len(l) == 0:
			print('No Values Entered')
			invalid_exit()
		else:
			print(f'Result = {divide_list(l)}')
			print('Exiting...')
			sys.exit(0)
	elif v.lower() == 'e':
		print('Exiting...')
		sys.exit(0)
	else:
		invalid_exit()
