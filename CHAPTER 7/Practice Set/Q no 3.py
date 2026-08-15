nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter:"))
idx = 0
for val in nums:
    if val == x:
        print(f"Num {val} found at index {idx}")
    idx += 1
