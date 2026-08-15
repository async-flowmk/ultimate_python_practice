# Simple list of MCU Superheroes
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
    "Wolverine",
]

# Print the list line-by-line
for hero in mcu_heroes:
      if hero == "Deadpool":
        print("Deadpool found")
        break
      print (hero)
else:
      print("**End of list**")

# Range function:
for i in range(5):# range(stop)
     print(i)

for val in range(2 , 8): # range(start , stop)
    print(val)
#output : 2,3,4,5,6,7

for num in range(2 , 20 ,4): #range(start, stop ,step)
      print(num)
# Output : 2 6 10 14 18

# String iteration:

s = "Ayra"
for i in s:
     print(i)