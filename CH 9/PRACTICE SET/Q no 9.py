censored_word = ["Donkey","Donkeys","animal"]


with open("CH 9/PRACTICE SET/file.txt", "r") as f:
    data = f.read()

for word in censored_word:
    data = data.replace(word,"*"*len(censored_word))

with open("CH 9/PRACTICE SET/file.txt", "w") as f:
    f.write(data)