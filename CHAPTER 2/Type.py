a = "Stranger Things" # This is a string
print(type(a))

b = 3.14 # This is a float (a number with a decimal point)
print(type(b))  

c = 42 # This is an integer (a whole number without a decimal point)
print(type(c))

d = True # This is a boolean (a value that can be either True or False)
print(type(d))

e = [1, 2, 3, 4, 5] # This is a list (a collection of items)
print(type(e))

f = {"name": "Alice", "age": 30} # This is a dictionary (a collection of key-value pairs)
print(type(f))

print(type(str(b))) # This converts the float b to a string and prints its type, which will be <class 'str'>

print(type(int("234"))) # This converts the string "234" to an integer and prints its type, which will be <class 'int'>

type_change = int(input("Enter a value: ")) # This takes user input as an integer
print("You entered:", type(type_change), type_change) # This prints the value entered by the user

print(type_change + 10) # This adds 10 to the user input and prints the result, which will be an integer