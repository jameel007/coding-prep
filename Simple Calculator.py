# Simple Calculator
## This is a simple calculator that can add, subtract, multiply, and divide two numbers.
""" Lets go a bit further and 
    handle the errors too.
We will use the try and except block to handle the errors."""

a = float(input("Enter the first numeric value:")) 
b = float(input("Enter the second numeric value:"))
Sum = a+b
Substraction = a - b
Multiplication = a * b
print("You have entered the first value as:", a)
print("You have entered the second value as:",b)
print("This is sum:",Sum)
print("This is Sub:",Substraction)
print("This is multiplication:",Multiplication)
if b ==0:
    print("Division by zero is undefined")
else:
    Div = a/b
    print("This is div",Div)
    floor_division = a//b
    print("This is floor division:", floor_division)
    modulus = a % b
    print("This is modulus:", modulus)
