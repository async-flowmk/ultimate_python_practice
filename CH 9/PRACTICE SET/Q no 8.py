word = input("Enter word: ").lower()

with open("CH 9/PRACTICE SET/file.txt", "r") as f:
    data = f.read()

new_word = data.replace(word, "####")

with open("CH 9/PRACTICE SET/file.txt", "w") as f:
    f.write(new_word)