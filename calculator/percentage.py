#Importing Sys
import sys

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
