# Question no 1: Find union, intersection, and difference of two sets.
set1 = {1,3,5,7,9}
set2 = {2,4,6,8,5,7,1}

union = set1.union(set2) #{1,2,3,4,5,6,7,8,9}
inter = set1.intersection(set2) # {5,7,1}
differ= set1.difference(set2) # {3,9}

print(f"""
      Union of set 1 and 2 is {union} , 
      Intersaction of set 1 and 2 is {inter} &
      Difference of sets is {differ}
""")


# Question no 2: Check if one set is a subset of another.

subset = set1.issubset(set2)

print(subset)