# Input Numbers
n1 = int(input("Enter a num:"))
n2 = int(input("Enter a num:"))
n3 = int(input("Enter a num:"))
n4 = int(input("Enter a num:"))

# Check greatest num
if (n1>n2 and n1>n3 and n1>n4):
    print("N1 is greatest num")
elif (n2>n1 and n2>n3 and n2>n4):
    print("N2 is greatest num")
elif (n3>n1 and n3>n2 and n3>n4):
    print("N3 is greatest num")
else:
    print("N4 is greatest num")

    # This is my logic and code 

# This improve by AI

Greatest = n1
if(n2 > Greatest):
    Greatest = n2
elif(n3 > Greatest):
    Greatest = n3
elif(n4 > Greatest):
    Greatest = n4

print(f"The greatest number is: {Greatest}")