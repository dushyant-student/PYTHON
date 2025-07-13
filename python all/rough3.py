#leap year dectaer
"""while True:
   l=int(input('enter year'))
   if (l%4)==0:
       print('yes, it is leap year!')
   else:
        print('this is not leap year!')
    
        


        
#largest no
print(" press "B" for exit")
l=[]
n=int(input("how many no?"))
for i in range(1,n+1):
    us=input('enter no')
    l.append(us)
print(l)
l.sort()
#print(l)
print('it in mininmum no',l[0])



#leap year program:
l=[]
e=str(input("Enter no:-"))
p=len(e)
if p<5:
    for i in range(0,4):
      k=e[i]
      l.append(k)
    print("your yr",l)
    k=l.join(l[-1],l[-2])
    int(k)
    if (int(k)%4)==0:
       print("this is leap year:-",e)
    else:
       print("not leap year:")
else:
    print("invalid year")


#leap yr using string 
while True:
    yr=int(input("Enter year:-"))
    if yr<1600:
        print("incorrct year")
    elif yr%4==0:
         print("Yes leap year!")
    else:
        print("Not leap year")
        break
        

#Sum of n natural no:-
n=eval(input("Enter sum of natural no:-"))
a=eval(input("Enter ist term "))
d=eval(input("Enter common diff:-"))
result=int(n/2*(2*a+n*d-d))
print(result)
print((n/2)*(2*a+(n-1)*d))




#greatest no range index no upto four only 
l=[]   
print("only four no will you insert:-")
for i in range(1,4):
    a1=int(input("enter no"))
    l.append(a1)
print(l)
if l[0]>(l[1] and l[2] and l[3]):
  print(l[0], "is greater than all no")
elif l[1]>(l[2] and l[0] and l[3]):
  print(l[1],"is greater than all")
elif l[2]>(l[3] and l[1] and l[0]):
    print(l[2],"is greater than all no")
else:
   print(l[3],"is greater than all")



#greatest no in Nth inputs no:
n=int(input("how will you insert  no of compersion;-"))
list=[]
for i in range(1,n+1):
  # print("enter no",i)
   us=int(input('enter no'))
   us.append(list)
print("Net elements of your choice:-",list)
for j in range()

   


#one no is divisible by another no:
i=int(input("Enter no:-"))
e=int(input("enter no:-"))
if e==0:
    print("take correct inputs!")
elif i%e==0:
    print(i, "is divisible by:- ",e)
else:
    print(i,"is NOT divisible by:- ",e)



#Decimal to bineary coverter: by using direct function 
dec=int(input("take decimal no:-"))
us=int(input("""what is convert?
                1.decimal to bineary?
                2.decimal to octal? 
                3.Hexa decimal?"""))
if us==1:
    print(dec,"the binary no is:-",bin(dec))
elif us==2:
    print(dec,"The octal no is:-",oct(dec))
elif us==3:
    print(dec,"the Hexadecimal no is",hex(dec))
else:
    print("this is not correct no for converting the bin to")



#ramdom generated bin no by random function!
import random 
dec=random.randrange(0,1000)
print(dec,"Random generated decimal (no b/w 0 to 1000) ")
us=int(input("""what do you to convert?
                1.decimal to bineary?
                2.decimal to octal? 
                3.decmal to Hexa decimal? 
                   """)) 
if us==1:
    print(dec,"the binary no is:-",bin(dec))
elif us==2:
    print(dec,"The octal no is:-",oct(dec))
elif us==3:
    print(dec,"the Hexadecimal no is",hex(dec))
else:
    print("this is not correct no for converting the bin to")











