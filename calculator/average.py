#Telling User How to Exit and Get Results
print('Enter E to Exit')
print('Enter R for Results')

#Predefined Values
#Average Formula :- Sum of all values (in this case, the list) / Number of values (Defined as l/byd)
l = list() #Creates Empty list
byd = 0 #Create a Variable with value 0


while True:
	v = input('Enter Number ' + str(byd + 1))
	if v.isnumeric():
		l.append(int(v))
		byd += 1
	elif v.lower() == 'r':
		print('Average = ' + str(sum(l)/byd))
		print(exit('Exiting...'))
	elif v.lower() == 'e':
		print(exit('Exiting...'))
	else:
		continue
