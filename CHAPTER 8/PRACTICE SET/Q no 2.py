# Recursive function to calculate sum:
def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n


print(cal_sum(65))

# Recursive function to print all elements of list:
mcu_heroes = [
    "Iron Man",
    "Captain America",
    "Thor",
    "Black Widow",
    "Hulk",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Scarlet Witch",
    "Captain Marvel",
    "Ant-Man",
    "Wasp"]
def print_elem(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_elem(list , idx+1)

print_elem(mcu_heroes )

