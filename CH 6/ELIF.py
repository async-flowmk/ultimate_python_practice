age = int(input("Enter your age:"))

if(age >= 18):
    print("Your ticket price is 2000 rupees")
elif(age < 18 and age >= 12):
    print("Your ticket price is 1500 rupees")
elif(age < 12 and age >= 6):
    print("Your ticket price is 1000 rupees")
elif(age < 0):
    print("You enter invalid age")    
else:
    print("you are free to go")

