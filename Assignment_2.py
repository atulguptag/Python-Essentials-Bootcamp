'''Assignment - 2
Create a python program to fill the values in three variables a,b,c

Rules* 1. The program will take the int value from the user between 1 to 60

2. Divide that int value into 3 variables (a,b,c) such that a can take max 20, b can take max 10, and c can take max 30

Example 1: Enter the value: 45
Answer
a = 20 c = 10 b = 15
or
a = 20 c= 25 b=0

Example 2: Enter the value: 61
Answer
Value must be less than or equal 60'''

n = int(input("Enter the value : "))

if n > 60:
    print("Value must be less than or equal to 60")
    exit(1)

a = (n < 20) * n + (n >=20) * 20
b = (n - a < 10) * (n - a) + (n - a >= 10) * 10
c = (n - a - b < 30) * (n - a - b) + (n - a - b >= 30) * 30

print(f"a = {a}, b = {b}, c = {c}")

