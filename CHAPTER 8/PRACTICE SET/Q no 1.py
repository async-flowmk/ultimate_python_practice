# Function to print the len of list:
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
    "Wasp",
    "Falcon ",
    "Winter Soldier",
    "Star-Lord",
    "Groot",
    "Rocket Raccoon",
    "Shang-Chi",
    "Ms. Marvel",
    "Moon Knight",
    "Deadpool",
    "Wolverine"
]

def list_len(list):
    print(len(list))
    return len(list)

list_len(mcu_heroes)

# Function to print element of list in single line:
def print_el(list):
    for item in list:
        print(item,end=" ")
    return item

print_el(mcu_heroes)
print()

# Function to print factorial of n numbers:
def calc_fact(n = int(input("Enter num:"))):
    fact = 1
    for val in range(1,n+1):
        fact *= val
    print(fact)
    return(fact)

calc_fact()

# Function to convert USD to PKR:
def conv_usd(usd=int(input("Enter num:"))):
    pkr = 277.30
    print(f"{usd}$ = {round(usd*pkr)} Rs")

conv_usd() 