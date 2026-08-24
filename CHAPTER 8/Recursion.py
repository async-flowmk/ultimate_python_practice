def show(n):
    if n == 0: # Base case
        return
    print(n)
    show(n-1)

show(5)# 5 , 4 = n-1 , 3 = n-2 , 2 = n-3 , 1 =    v n-4   

def fact(n):
    if n==0 or n==1:
        return n
    else:
        return fact(n - 1)*n

print(fact(5))