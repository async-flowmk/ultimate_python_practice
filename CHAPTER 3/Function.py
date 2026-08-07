str = "This is a string"

# Len Function (print length of a string.):
print(len(str)) # output 16

# endswith Function (print ending of string is true or false):
print(str.endswith("string"))  # output True

# startswith Function (print starting of string is true or false):
print(str.startswith("This"))  # output True

# Find function (print the index of find word):
print(str.find("a")) # output 8

# Replace function 
text = "I like Python"
print(text.replace("Python", "AI"))  # I like AI

# Split function
text = "apple banana mango"
print(text.split())  # ['apple', 'banana', 'mango']

# Lower or Upper function 
text = "Hello"
print(text.lower())  # hello
print(text.upper())  # HELLO