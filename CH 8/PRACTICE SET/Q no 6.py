# Recursive program to calc sum of first n num:
def calc_sum(n):
    if n == 0:
        return 0
    return calc_sum(n-1) +n

print(calc_sum(10))

# n = 10
# calc_sum(10 - 1)  + 10 = 19
# n = 9 
# calc_sum(9 - 1)  + 9 = 17
# n = 8
# calc_sum(8 - 1)  + 8 = 15
# n = 7
# calc_sum(7 - 1)  + 7 = 13
# n = 6
# calc_sum(6 - 1)  + 6 = 11
# n = 5
# calc_sum(5 - 1)  + 5 = 9
# n = 4
# calc_sum(4 - 1)  + 4 = 7
# n = 3
# calc_sum(3 - 1)  + 3 = 5
# n = 2
# calc_sum(2 - 1)  + 2 = 3
# n = 1
# calc_sum(1 - 1)  + 1 = 1

# n = 0 
# if n == 0:
#   return 0
