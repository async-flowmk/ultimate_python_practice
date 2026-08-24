# function to print greatest num:
def in_int():
    return int(input("Enter a number: "))

def cal_great_num():
    num = int(input("How many numbers do you want to compare? "))
    if num <= 0:
        return
    # Initialize 'greatest' with the first number
    greatest = in_int()
    # Loop for the remaining (num - 1) numbers
    for _ in range(1, num):
        val = in_int()
        if val > greatest:
            greatest = val
            
    print(f"The greatest number is {greatest}")

cal_great_num()



# def in_int():
#     inp = int(input("Enter a number:"))
#     return inp

# def cal_great_num():
#     num = int(input("How many numbers do you find greatest :"))
#     for val in range(1,num+1):
#         val = in_int()
#         greatest = val
#         if val <= 0:
#             return val 
#         else:
#             if val > greatest:
#                 greatest = val
#     print(f"The Greatest number is {greatest}")

# cal_great_num()
        
