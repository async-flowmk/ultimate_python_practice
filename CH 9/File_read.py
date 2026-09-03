file = open("CHAPTER 9/sample.txt","r")
# data = file.read()
line1 = file.readline()
line2 = file.readline()
print(f"Sample.txt line no 1 is:{line1}",end="")
print(f"Sample.txt line no 2 is:{line2}")
# print(data)
file.close()

