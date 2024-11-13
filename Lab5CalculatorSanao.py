choice = int(input("Calculator\n"
                   "1. Add\n"
                   "2. Subtract\n"
                   "3. Multiply\n"
                   "4. Divide \n"
                   "Choose 1-2-3-4: "))

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Cannot divide by ZERO.")
    else:
        return x / y

if choice == 1:
    print("------------------------------")
    print(f"The sum is: {add(a, b)}")
elif choice == 2:
    print("------------------------------")
    print(f"The difference is: {subtract(a, b)}")
elif choice == 3:
    print("------------------------------")
    print(f"The product is: {multiply(a, b)}")
elif choice == 4:
    print("------------------------------")
    print(f"The quotient is: {divide(a, b)}")
else:
    print("------------------------------")
    print("Invalid Input.")