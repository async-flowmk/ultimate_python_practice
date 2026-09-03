s1 = {1,4,5,6,2}
s2 = {1,7,3,6,2}

set_union = s1.union(s2) # Combine sets
print(set_union) # {1,2,3,4,5,6,7}

set_inter = s1.intersection(s2) # Common element on both sets
print(set_inter) # {1,2,6}
