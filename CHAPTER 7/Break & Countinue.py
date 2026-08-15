# Break : Used to terminate loop where you want

i = 0
while i <= 10:
    print(i)
    if i == 8:
        break
    i += 1

# Continue : Terminate current iteration 

a = 0 
while a <= 10 :
    if a % 2 != 0 :
        a += 1
        continue
    print(f"{a}")
    a += 1