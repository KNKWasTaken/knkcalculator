#Telling User How to Exit and Get Results
print('Enter E to Exit')
print('Enter R for Results')

#Predefined Values
#Average Formula :- Sum of all values (in this case, the list) / Number of values (Defined as l/byd)
l = list() #Creates Empty list
byd = 0 #Create a Variable with value 0


while True:
	v = input('Enter Number ' + str(byd + 1) + ' :')
	if v.isnumeric():
		l.append(int(v))
		byd += 1
	elif v.lower() == 'r':
		if byd == 0:
			print('No Values Entered')
			invalid_exit = input('Do You Want To Exit? (y/n): ')
			if invalid_exit.lower() == 'y':
				print(exit('Exiting...'))
			elif invalid_exit.lower() == 'n':
				print('Continuing with Calculation.')
			else:
				print('Invalid Value Entered. Continuing with Calculation.....')
		else:
			print('Average = ' + str(sum(l)/byd))
			print(exit('Exiting...'))
	elif v.lower() == 'e':
		print(exit('Exiting...'))
	else:
		print('Invalid Argument...')
