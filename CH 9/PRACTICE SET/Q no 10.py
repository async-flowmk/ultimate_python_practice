with open("CH 9/PRACTICE SET/log.txt") as f:
    content = f.read()
    if "python" in content :
        print("Yes python word exist.")
    else:
        print("Yes python word not exist.")
