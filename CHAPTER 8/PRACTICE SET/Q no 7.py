def rev_star(n):
    if n == 0:
        return 
    else:
        print("*" * n,end="")
        print("")
    rev_star(n - 1)

rev_star(5)