"""j=int(input("Enter fact no :-", ))
for h in range(1,j+1):
    print(h)

n=int(input("Enter no of elements:-",    ))
l=[]
for i in range(1,n+1):          # W
    e=int(input("enter no", ))
l.append(e)
print(l)


#def larg(a,b,c,d):
 # l=[a,b,c,d]
k=[]
for i in range(0,4):
    m=int(input('enter you no:-', ))
    k.append(m)
print(k)
if k[0]>k[1] and k[0]>k[2] and k[0]>k[3]:
    print('greatest no is:-',k[0])
if k[1]>k[0] and k[1]>k[2] and k[1]>k[3]:
      print('your greatest no is:-', k[1])
if k[2]>k[1] and k[2]>k[0] and k[2]>k[3]:
        print('greatest no is :-', k[2])
else:
    print('greatest no is:-',k[2])




###2nd method by funstion of sort using:-
list=[]
for j in range(0,4):
     us=int(input("Enter your no:-",  ))
     list.append(us)
print(list)
list.sort()
print(list,"the greatest no is in list is:-",list[3])
"""






#return statment 
"""def bin(s):
 for k in range(s):
    hi=int(input('Enter your no:-'))
    ug=[]
    ug.append(hi)
print(ug)
if ug[0]>ug[1]:
    print(ug[1])
return ug[0]
t=bin(3)
print(t)


#stack using opperations 
#thatswork but why is error is found in 2 choive not push ele show none
l=[42,48,27,3,99,16,4,39,32,64,37,4,88]
while True:
    n=int(input("""enter your choice:-
            1. push(append)
            2.delete:-
            3.front(del)
            4.rear(push)
            Enter your choice:-"""))
    if n==1:
        if len(l)!=14:
           us=int(input("Enter your push ele:-",))
           k=l.append(us)
           print(k)
        else:
            print("you are not able to append ele size is over(over flow)!")
    elif n==2:
        if len(l)==0:
            print("size is zero not append ele underflow:-")
        else:
           l.pop(-1)
           print("your ele is delete :-",l)
    elif n==3:
        if len(l)!=0:
            print("front(last value) ele is:-",l[-1] )
        else:
            print("stack is empty")
    elif n==4:
        if len(l)==0:
            print("stack is empty you can't append ele:-")
        else:
         print("rear ele is:-",l[0])
    else:
        print("invalid input:-")
        break
"""











        


