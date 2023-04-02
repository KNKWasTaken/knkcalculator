import knkcalculatorfuncsheet

print("Welcome to KNKCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Average")
print("6. Percentage")

while True:
    operator = input("Enter Operator (1-6): ")
    if operator == "1":
        knkcalculatorfuncsheet.addition()
    elif operator == "2":
        knkcalculatorfuncsheet.subtraction()
    elif operator == "3":
        knkcalculatorfuncsheet.multiplication()
    elif operator == "4":
        knkcalculatorfuncsheet.division()
    elif operator == "5":
        knkcalculatorfuncsheet.average()
    elif operator == "6":
        knkcalculatorfuncsheet.percentage()
    else:
        knkcalculatorfuncsheet.invalid_exit()