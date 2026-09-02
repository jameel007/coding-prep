## Calculator with Conditional Statements
## Ask the user for Operator to perform the calculation
a = float(input("Enter first numerical value: "))
b = float(input("Enter second numeric value: "))
op = input("Enter the operator you want: + , - , *, //: ")
if op == "+":
    print("The Sum is:", a + b)
elif op == "-":
    print("The Sub is:", a - b)
elif op == "*":
    print("The Mul is:", a * b)
elif op == "//":
    if b == 0:
        print("Error : Zero is not a Divisible value for Division")
    else:
        print("The Division is:", a // b)
else:
    print("Input Error: Please pick values from the given choice")








