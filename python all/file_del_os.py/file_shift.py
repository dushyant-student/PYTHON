import os 
fake="fakefile.txt"
file2= "fake-file_shift.txt"
with open(fake,"r") as f:
    f.read()
    with open(file2,"w") as f2:
        f2.write(fake)
        os.remove(fake)
        

