def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Please select operation: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

operator = int(input("Select operations form 1, 2, 3, 4: "))
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if operator == 1:
    print(f"{first} + {second} = {add(first,second)}")
elif operator == 2:
    print(f"{first} - {second} = {subtract(first,second)}")
elif operator == 3:
    print(f"{first} * {second} = {multiply(first,second)}")
elif operator == 4:
    print(f"{first} / {second} = {divide(first,second)}")
else:
    print("Invalid")