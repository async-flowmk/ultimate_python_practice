# Generate multiplication table from 2 to 20 in Tables folder :
def generate_table(n):
    table = ""
    for i in range(1,11):
        table += (f"{n} x {i} = {n*i}\n")
        with open(f"CH 9/PRACTICE SET/Tables/Table_{n}.txt","w")as f:
            f.write(table)
start_table = int(input("Enter where you start to print:"))
end_table = int(input("Enter where you end to print:"))
for i in range(start_table,end_table+1):
    generate_table(i)



    