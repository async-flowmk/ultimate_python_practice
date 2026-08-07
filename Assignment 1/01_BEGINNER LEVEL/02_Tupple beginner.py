# Question no 1: Create a tuple with 5 elements and print the first and last element.

tup = ("ali","24",5,5,"mustafa")

print(tup[0:5:4])# ("ali","mustafa")


# Question no 2: Convert a tuple into a list

convert = list(tup)
print (convert)

# Question no 3: Count how many times a value appears in a tuple.

print(tup.count(5))