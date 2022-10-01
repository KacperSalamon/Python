#Python calucalator NON GUI

print("Select operation which you want use: ")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

operation = input()


if operation == "1":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    print("The sum operation is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    print("The sum operation is " + str(int(num1) - int(num2)))
elif opertation == "3":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    print("The sum operation is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    print("The sum operation is " + str(int(num1) / int(num2)))
else:
    print("Invalid values or Entry")
