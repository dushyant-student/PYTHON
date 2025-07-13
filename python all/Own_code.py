"""#1. SUM OF N NATURAL NUMBER WITH USER INPUT at last digit:-

n=int(input("enter your number for n sum:- ", ))
s=(n*n+n)/2   
print("the sum of your number for n sum:-",s)"""


"""
#2. SUM OF ANY N TERMS BY ACCORDING TO USER INPUT:- 

a=eval(input("enter your first digit(a) :-", ))
n=eval(input("enter no of term:- ", ))
d=eval(input('enter your common diff :- ', ))
sum=int((n*a)+(n*n*d-n*d)/2)  #if you apply oper on any no we don't need comma(,) for simplification 
print(" the sum of your AP series of ",n,"th term is :- ", sum )




#SUM OF GEOMETRIC SERIES OF N TERMS:-
a=eval(input("enter your start no(first no ):- ", ))
r=eval(input("enter your common ratio(R) :- ", )) #FORMULA WRONG 
n=int(input("enter your no of terms:- ", ))
sum=a*(r**n-1)
print("the sum of gp of ",n,"th term is:- ", sum)





#UPDATE ANY CHARACTER OR VALUE IN GIVE LIST:-
L=["+",1,2,3,"$","&","*","8","@","N",]
N=eval(input("Enter index no :-", ))
V=str(input("assign value write:- ", ))
L[N]=V
print("your new list have created :-",L)





#UPDATE multi CHARACTER OR VALUE IN GIVE LIST  in contnous indexing with range loop :-
L=["+",1,2,3,"$","&","*","8","@","N",]
p=eval(input("enter your starting idex no :- ", ))
t=eval(input("enter last index no:- ", ))
for N in range(p,t+1):
 V=str(input("assign value write:- ", ))
L[N]=V
print("your new list have created :-",L)  #how to print n times


#find space bar in any name by user input:-
us=input("enter your name without space :-", )
p=us.find(" ")
print("You have double space in your name line index no",p ,"please correct this name :-" 



#remove space bare in any user name:-
op=input("enter your name", )
sd=op.replace(" ")                   # not work because replace at least have two argument not one argument! 
print("hello!",sd )      


#replace a spicfice word or remove ? in any name:-
pd =input("enter your name withoubut quistion mark:-", )   #assign only those name which hase ? mark.
l=pd.replace("?","_")
print("your name has ? please correct this name:-",l)



#replace a spicfice word or remove ? in any name:-
pd =input("enter your name without quistion mark:-", )
t="?"
if t in pd:                            #type any types of name  NOTE :- string does not support remove syntex 
 l=pd.replace("?","_")
 print("your name has ? please correct this name:-",l)
else:
 print("your name is :-",pd )




#Using remove syntex in list make remover ? in any name 
list=input("Enter your name without ? mark:-", )
list2=[list]
list2.remove("?")     # NOT WORK remove works only on indexing not contious in dict word lining !
print(list2)



#program to reverse any no or string:-
us=input('enter no or str:-', )
l=len(us)-1
for i in range(l,-1,-1):  #Reverse l goes upto 0 ,for -1 with -1 decrement!
    k=us[i]
    print(k,end="")


#program of perfect no! ex:-6 is perf no.because 1,2,3 is fect of 6 and adding to this gives 1+2+3=6
s=0
us=int(input('Enter a perfect no:-', ))
for i in range(2,us-1):
    k=us%i
    if k==0:
     s=s+i
print("sum of this no:-",s+1) 
if s+1==us:              #i=i+s    
    print('it is a perfect no:-',s+1)
else:
    print('this no. not a perfect no.:-',s+1)


                    #BOTH HAS SAME PROG BUT DIFFERNT METHOD:-


#program of perfect no! ex:-6 is perf no.because 1,2,3 is fect of 6 and adding to this gives 1+2+3=6

s=1
g=int(input('enter perfect no:-', ))
for i in range(2,(g//2)+1):
    k=g%i
    if k==0:
      s=s+i
if s==g:
   print('sum of this no. is equal to user i/p:-',s,'so, this no is perfect no:-',g)
else:
   print('sum of this no. is not equal to user i/p:-',s,'so, this no. is not a perfect no:-',g)


# find factorial any no:-
n=int(input("enter your no:-"))
for j in range(n,0,-1):
print(n)
"""

#find lcm of 2 no:-   NOt work!   
while True:
    a1=int(input("Enter no 1 :-"))
    a2=int(input("Enter no 2 :-"))
    for i in range(2,500):
        if (i%a1 and i%a2)==0:
            lcm=i
        print(lcm)
        break
    if (a2%a1)!=0:
        print("LCM is:- ",a1*a2)
    elif a2%a1==0:
        print("LCM is:- ",a2)
    elif a1%a2!=0:
         print(a1*a2)
    elif (a1 or a2)==0:
            print("lcm is:- 0")
    if a1%a2==0:
        print("Lcm is:- ",a1)
    else:
        print("invalid input")
        break 

