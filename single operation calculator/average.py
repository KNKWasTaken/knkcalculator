#Importing sys
import sys

#Creating Exit Function for Inavlid Data
def invalid_exit():
	invexit = input('Do You Want To Exit? (y/n)')
	if invexit.lower() == 'y':
		print('Exiting...')
		sys.exit(0)
	elif invexit.lower() == 'n':
		print('Continuing With Calculation...')
	else:
		print('Invalid Data. Continuing With Calculation...')

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
			invalid_exit()
		else:
			print('Average = ' + str(sum(l)/byd))
			print('Exiting...')
			sys.exit(0)
	elif v.lower() == 'e':
		print('Exiting...')
		sys.exit(0)
	else:
		invalid_exit()
