# Python Set Methods

# Creating a set
my_set = {1, 2, 3, 4, 5}

# add() - Add a single element
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# remove() - Remove an element (raises KeyError if not found)
my_set.remove(6)

# discard() - Remove an element (no error if not found)
my_set.discard(1)

# pop() - Remove and return an arbitrary element
element = my_set.pop()

# clear() - Remove all elements
# my_set.clear()

# union() or | - Combine sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}

# intersection() or & - Common elements
intersection_set = set1.intersection(set2)  # {3}

# difference() or - - Elements in first set but not in second
diff_set = set1.difference(set2)  # {1, 2}

# symmetric_difference() or ^ - Elements in either set but not both
sym_diff = set1.symmetric_difference(set2)  # {1, 2, 4, 5}

# issubset() - Check if one set is subset of another
print(set1.issubset(set2))  # False

# issuperset() - Check if one set is superset
print(set1.issuperset(set2))  # False

# copy() - Create a shallow copy
set_copy = set1.copy()

# len() - Get number of elements
print(len(set1))  # 3