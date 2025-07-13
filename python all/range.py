"""l=[10,20,30,40,50,56,57,60,67.7,70,79.7777]
f=len(l)   
u=eval(input('enter search ele:-',  ))
for j in range(f):
    if l[j]<u<l[j+1]:
        print(l[j],'between',l[j+1])
        





#shuffel list elemens by using function of suffel:
import random
list=[]
us=int(input("enter no:- "))
for i in range(0,us): 
    u=str(input("enter no:- "))
    k=list.append(u)
print("your list:- ",k)
print("Shuffeld list:- ",random.shuffle(k))


j=[2,3,4,5]
for k in j:
    print(k)
    


#NOTE ##############
for j in range(0,8):
    print((len(str(j))))


start=int(input("Enter where your start? :- "))
last=int(input("Enter your last no:- "))
for j in range(start,last):
    amst=0
    k=len(str(j))
    print(k)
    print(j)
    


#typing
list=[]
str="my name is dushyant hoo are you"
ip=input("lets typing:- ")
p=len(str)
for j in range(0,p):
   if str[j]!=ip[j]:
      list.append(ip[j])
      print("mistake at:- ",j,"word:- ",str[j])
print(list)

"""
i=0
for i in range(0,6):
    i=i+1
print(i)

