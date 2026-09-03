# # Print numbers from 100 to 1:

# a = 100
# while  a >= 1:
#     print(a)
#     a -= 1

# # print the multiplication table of a number n :
# n = int(input("Enter a num :"))
# i = 1

# while i <= 10:
#     print(f"{n} x {i} = {n*i}")
#     i += 1

# # prin the elements of the following list using a loop:

# l = [1,4,9,16,25,36,49,64,81,100]

# c = 1
# while c < len(l):
#     print(l[c])
#     c += 1

# Search for a num x in the tuple using loop :
nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("What num you find :"))
if x in nums :
    idx = 1
    while idx < len(nums):
        if nums[idx] == x:
            print(f"{x} is present in num(tuple)")
            idx += 1
else :
    print("Not found")    



