# Question no 1: Create a dictionary of 3 students with marks and print all keys.

marks = {
    "Hamza" : 68,
    "Raniya": 95,
    "Imsaal": 98
}
dict_keys = marks.keys()
print(dict_keys)

# Question no 2: Print all values of a dictionary.

dict_values = marks.values()
print(dict_values)

# Question no 3: Update a value in a dictionary.

dict_update = marks.update({"Imsaal":98.9})
print(marks)