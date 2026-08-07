dict = {} # Empty dictionary

marks = {
    "Ali"    :89,
    "Mustafa":91,
    "Hassan" :57,
    "Mujeeb" :78,
    "Aliyan" :82
} 
# 1 Items method:

print(marks.items())

# 2 Keys method:

print(marks.keys())

# 3 Update method :

marks.update({"Mustafa":93})
print(marks)

# 4 Get method:
"""
The differance between 'get' and '[]' is , if the key does no exist the get method gives none . Other side [] method gives error .
for example
print(marks.get("Aliyan2")) # output = none
print(marks["Aliyan"]) # output = error
"""
# print(marks.get("Aliyan2")) # output = none
# print(marks["Aliyan2"]) # output = error

print(marks.get("Aliyan")) 

# Pop method 

marks.pop("Hassan")
print(marks)

# len  method

print(len(marks))
print(marks)