#Question no 1 : Write a program using logical operators (and, or, not).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a < b OR a > b:", (a < b) or (a > b))
print("a < b AND a > b:", (a < b) and (a > b))
print("NOT (a > b):", not (a > b))
print("NOT (a < b):", not (a < b))
#Question no 2 : Use membership operators (in, not in) on a list.

basket = ["Apple","Banana","Grapes","Watermelon","Mango"]

print("Apple" in basket) # True
print("Starberry" not in basket) # true
print("Berries"  in basket) # false