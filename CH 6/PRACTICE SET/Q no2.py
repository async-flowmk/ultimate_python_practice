# Subject marks :

physics = int(input("Enter physics marks:"))
maths = int(input("Enter math marks:"))
chemistry = int(input("Enter chemistry marks:"))

total_marks = 300
obtained_marks = physics + maths + chemistry

if (obtained_marks > total_marks):
    print("Enter wrong marks")
else:
    percentage = obtained_marks / total_marks * 100
    print(f"you obtained {obtained_marks} marks in exam and your percentage is {percentage}")
    if(percentage >= 85):
        print("passed , Grade A+")
    elif percentage >= 75:
        print("passed , Grade A")
    elif percentage >= 65:
        print("passed , Grade B+")
    elif percentage >= 55:
        print("passed , Grade B")
    elif percentage >= 40:
        print("passed , Grade C")
    else:
        print("Failed")    

sub1 = physics / 100 *100
sub2 = maths / 100 *100
sub3 = chemistry / 100 *100

if(sub1  < 33):
    print("failed in physics")
elif(sub2 < 33):
    print("failed in maths")
elif(sub3 < 33):
    print("failed in chemistry")
else:
    print("passed in all subjects")



 


