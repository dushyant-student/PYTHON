'''file=open("file.txt","r")      #open file in read mode
g=file.read()
print(g)
file.close()


#append new line in file and  remove previous line (data)!
f=open("file.txt","w")
f.write("i am not for you")
f.close()



#write many lines in tet file 
f=open("file.txt","a")
f.write("i am honesty man ")
f.write(""" and you are foolish man 
and you are not for me """)
f.close()


#open file in read mode and read no. line 
file=open("file.txt","r")
g=file.readline()
print(g)
file.close()


#file open amd remove previous line or Enter new line
openfile=open("file.txt","w")
openfile.write("""yes i am succesfull for removing this text!  , not i am able to add to privous text!""")
openfile.close()



#Can open file read or write mode with statment as allias and getting benifit automattically file close!

with open("newfile.txt", "w") as f:
 j=f.write("append is pass!")
print(j)


with open("newfile.txt", "r") as t:
 f=t.read()
print(f)   '''
