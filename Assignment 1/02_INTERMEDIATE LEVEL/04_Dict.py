# Question no 1: Count frequency of each character in a string using a dictionary. 
text = "banana"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

# Question no 2: Merge two dictionaries.

dict1 = {
    "Ali":55,
    "Mustafa":89
}
dict2 = {
    "Imsaal":98,
    "Dua"  : 78
}

merge = dict1 | dict2
print(merge)

# 🧠 What is | ?

# This is called the merge (union) operator for dictionaries.


# Question no 3: Find the key with maximum value.

val = max(dict1, key=dict1.get)

print(val,dict1[val])