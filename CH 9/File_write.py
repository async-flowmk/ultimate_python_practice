file = open("CHAPTER 9/demo.txt","w")
file.write("Learning How to write in file.\n")
file.close()


f = open("CHAPTER 9/demo.txt","a")
f.write("\n My First female friend was ayra.")
f.close()

newfile = open("CHAPTER 9/mode.txt","w")
newfile.write("w = write \na = append \nr = read \nx = create new file \n+ = Dual purpose modifier \nr+ = read and write \nw+ = write and read \na+ = append and read")