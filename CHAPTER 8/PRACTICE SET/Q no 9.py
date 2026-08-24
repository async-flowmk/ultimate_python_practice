# function to remove a given word from a list ad strip it at same time:

def rem(list,word):
    n = []
    for item in list :
        if not (item == word):
            n.append(item.strip(word))
    return n
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
print(rem(mcu_heroes,"Man"))

