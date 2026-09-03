#  Function defination
def calc_sum(a , b):
    sum = a + b
    print(sum)
    return sum

calc_sum(8,2) 

#  Average of numbers :

def in_int():
    inp = int(input("Enter a number:"))
    return inp

def calc_avg():
    avg_num = int(input("How many num avg do you want:"))
    for i in range(1 , avg_num + 1):
        val = in_int()
        val += i
    avg = val / avg_num
    return avg

print(f"Average of four num = {calc_avg()}")


   