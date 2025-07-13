#Number is amstrong or not?
while True:
        us=str(input("Enter Number:-  "))
        k=len(us)
        print(k)
        amst=0
        for i in range(0,k):
            amst=(int(us[i])**int(k))+amst
        print("ams no  ",amst)
        if amst==int(us):
            print("Yes , this is amstrong no:-  ",us)
        else:
             print("this is not amstrong no! ", amst)


        
#Amstrong  no bt range
#this is working and correct program

while True:
    start=int(input("Enter where your start? :- "))
    last=int(input("Enter your last no:- "))
    list=[]
    for j in range(start,last):
        amst=0
        p=str(j)
        k=len(p)
        for s in range(0,k):
            amst=(int(p[s])**k)+amst
        print(j,"=", amst)
        if amst==int(p):
            list.append(int(p))
        print(list)

