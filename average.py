#Telling User How to Exit and Get Results
print('Enter E to Exit')
print('Enter R for Results')

#Predefined Values
#Average Formula :- Sum of all values (in this case, the list) / Number of values (Defined as l/byd)
l = list() #Creates Empty list
byd = 0 #Create a Variable with value 0


while l.isnum: #Checks if 
	v = input('Enter Number ' + str(byd + 1))
	l.append(int(v))
	byd += 1
elif l.lowercase == 'r':
	print('Average = ' str(sum(l)/byd))
	print(exit('Exiting...'))
elif l.lowercase == 'e':
	print(exit('Exiting...'))
else:
	continue
