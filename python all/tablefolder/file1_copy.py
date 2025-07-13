with open("file.txt","r") as c:
    p=c.read()                                  #not work!
with open("file1_copy.txt","w") as p:
    p.write(str(p))