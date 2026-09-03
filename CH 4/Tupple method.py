a = (1,2,3,5,6,7,4,9,8,56,4,6,34,7,3,73,7,3)

print(a.count(3))

print(a.index(34))

# ✅ len()
t = (1, 2, 3)
print(len(t))  # 3

# ✅ max() and min()
t = (5, 2, 9, 1)
print(max(t))  # 9
print(min(t))  # 1

# ✅ sum()
t = (1, 2, 3, 4)
print(sum(t))  # 10

# 🔹 Tuple Packing & Unpacking (VERY USEFUL 🔥)
# Packing
t = (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)  # 1 2 3

# 👉 This is used a lot in real coding (especially in loops, functions, etc.)

# 🔸 Convert tuple ↔ list
t = (1, 2, 3)

l = list(t)      # tuple to list
t2 = tuple(l)    # list to tuple