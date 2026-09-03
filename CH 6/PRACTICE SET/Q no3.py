# Input Comment
from builtins import input, any, print
comment = input("Enter your comment:")

# Spams list
sp_list = ["make a lot of money","buy now","subscribe this","click this"]

if any(phrase in comment for phrase in sp_list):
    print("This is a spam comment")
else:
    print(comment)