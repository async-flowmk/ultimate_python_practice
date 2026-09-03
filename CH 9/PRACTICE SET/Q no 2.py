# Function to change Java word with python:

def chng(word1,word2):
    file = open("CHAPTER 9/PRACTICE SET/practice.txt","r+")
    rep = file.read()
    new_data = rep.replace(word1,word2)
    file.write(new_data)
    print(new_data) 

chng("Java","Python")