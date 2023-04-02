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

def division():
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
                print(f'Sum = {sum(l)}')
                print('Exiting...')
                sys.exit(0)
        elif v.lower() == 'e':
            print('Exiting...')
            sys.exit(0)
        else:
            invalid_exit()

def multiplication():
    multiply_list = lambda list: 0 if len(list) == 0 else (list[0] if len(list) == 1 else list[0] - multiply_list(list[1:]))

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
                print(f'Result = {multiply_list(l)}')
                print('Exiting...')
                sys.exit(0)
        elif v.lower() == 'e':
            print('Exiting...')
            sys.exit(0)
        else:
            invalid_exit()

def addition():
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
                print(f'Sum = {sum(l)}')
                print('Exiting...')
                sys.exit(0)
        elif v.lower() == 'e':
            print('Exiting...')
            sys.exit(0)
        else:
            invalid_exit()

def subtraction():
    subtract_list = lambda list: 0 if len(list) == 0 else (list[0] if len(list) == 1 else list[0] - subtract_list(list[1:]))

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
                print(f'Result = {subtract_list(l)}')
                print('Exiting...')
                sys.exit(0)
        elif v.lower() == 'e':
            print('Exiting...')
            sys.exit(0)
        else:
            invalid_exit()

def average():
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

def percentage():
    #Telling User How to Exit
    print('Enter E to Exit') #Informs User about Early Exit System

    #User Input + Early Exit System
    #Formula of Percentage:- Part/Whole (defined as p and w)
    p = input('Enter Part:- ') #Take input from user about part value (input as string)
    if p.lowercase == 'e':
        print('Exiting...')
        sys.exit(0) #Converts p to lowercase and checks if it is 'e'. If it is e then it exits
    w = input('Enter Whole:- ') #Take input from user about whole value (input as string)
    if w.lowercase == 'e':
        print('Exiting...')
        sys.exit(0) #Converts w to lowercase and checks if it is 'e'. If it is e then it exits

    #Calculation + Print + Main Exit System
    print('Percentage = ' + str(int(p)/int(w))) #Prints "Percentage =" and then converts p and w to integers (and performs the calculation). After calculation, it prints the string result of the calculation (to avoid concatenate error)