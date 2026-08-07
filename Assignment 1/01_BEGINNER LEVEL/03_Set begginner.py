# Question no 1: Create a set and remove duplicate values from a list.

list = [1,2,3,2,4,3,5,6,5,6,7,5,8,9]

unique_list = set(list)

print(unique_list)#{1,2,3,4,5,6,7,8,9}

# Question no 2: Find common elements between two sets.

set1 = {1,15,25,36,48,5,6}
set2 = {24,35,15,2,6,78,9}

set_inter = set1.intersection(set2)
print(set_inter)# {15,6}

# Question no 3: Add and remove elements from a set.

set1.remove(48)
set1.add(45)

print(set1)