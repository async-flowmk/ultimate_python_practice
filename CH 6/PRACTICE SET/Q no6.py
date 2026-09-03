marks = int(input("Enter your exam marks:"))

if(marks >= 90 and marks <= 100):
    print(f"On {marks} your grade is A+ Excellent! ")
elif (marks >= 80 and marks <= 90 ):
    print(f"On {marks} your grade is A Good! ")
elif (marks >= 70 and marks <= 80 ):
    print(f"On {marks} your grade is B Average! ")
elif (marks >= 60 and marks <= 70 ):
    print(f"On {marks} your grade is C Under Average! ")
elif (marks >= 50 and marks <= 60 ):
    print(f"On {marks} your grade is D Need improve! ")
elif (marks < 50):
    print(f"On {marks} your grade is Fail ")
else:
    print("You enter invalid marks")
