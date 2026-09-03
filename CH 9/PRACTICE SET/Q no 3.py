# Search "Learning" in file:
def check_word():
    word = "learning"
    with open("CHAPTER 9/PRACTICE SET/practice.txt","r") as f:
        data=f.read()
        if data.find(word) != -1:
            print("Found")
        else:
            print("Not found")

# Find line:
def find_line():
    word = "learning"
    data = True
    line_no = 1
    with open("CHAPTER 9/PRACTICE SET/practice.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1
find_line()


        
