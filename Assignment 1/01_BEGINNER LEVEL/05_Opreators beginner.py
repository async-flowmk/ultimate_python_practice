# Question no 1: Take two numbers and perform all arithmetic operations.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

print(num1 + num2)  # Additio
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division
print(num1 % num2)  # Modulus (It gives the remainder after division.)
print(num1 ** num2)  # Exponentiation
print(num1 // num2)  # Floor division


# Question no 2: Compare two numbers using comparison operators.

a = 5
b = 8
print (a == b) # Equality
print(a > b) # Greater than
print(a < b) # Less than
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to
print(a != b) # Not equal to

# output
"""
1. false
2. false
3. true
4. false
5. true
6. true
"""

# Question no 3: Check if a number is even or odd using operators.

if num1 % 2 == 0:
    print("even")
else:
    print("odd")