with open("CH 9/PRACTICE SET/poem.txt","w+")as poem:
    data = poem.write("""Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
      """)
    poem.seek(0)
    data = poem.read().lower()
    word = input("Enter word:")
    if word not in data:
        print(f"{word} is not found")
    else:
        print(f"{word} is  found")
