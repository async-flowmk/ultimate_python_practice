with open("CHAPTER 9/PRACTICE SET/num.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    count = 0
    for val in nums:
        if int(val) % 2 == 0:
            count += 1
        else:
             (f"{val} is odd")
    print(count)





 

