## Building a small student pass with conditional statements
age = int(input("Please Enter your Age: "))
is_student = input("Are you a student? Y/ N: ").lower()
if age == 18:
    price = "$100"
elif age < 18:
     if is_student == "Y":
        price = "$FREE"
elif age == 12:
    price = "$30"
elif age == 60 and is_student == "n":
    price = "$1000"
else :
    price = "$0"
print("This is the Ticket fare:",price)

