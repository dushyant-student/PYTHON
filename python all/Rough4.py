"""#sum of natural no by using recursuion 
import random
r=random.randint(1,100)
def recur(n):
    print(r,"Th term according to recirsion, sum of 1st natural no ",(n*n+n)//2)
recur(r)




#find ASCI of chracter (all ascii values of are in a line)
while True:
    l=[]
    a=str(input("Enter alphabet of abcd:-"))
    for i in range(0,len(a)):
        k=a[i]
        print("ASCII representation on alphabets:-",ord(k),end=" ")
    if a!=str(a):
        break


#converter (find ASCII of  character) all ascii values in list 
l=[]
while True:
    us=str(input("enter alphabets:-"))
    for j in range(0,len(us)):
        l.append(ord(us[j]))
    print("list of ACSI(converter) values:- ",l)



#find lcm of 2 no:-   
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
        


     """ """  for j in range(us,last+1): #Wrong why?
    for i in range(2,j):
        if j%i==0:
            break 
        print(j,"is not prime no")
        print(j)"""  """
            


#taking user input find it is prime no or not?
while True:
    us=int(input("Enter a no:-"))
    for i in range(2,us):
        if us%i==0:
            print(us,"it is not a prime no")
            break
        elif us==1:
            print("1 , not prime no")
    else:
        print(us,"Yes, it is prime no!")


"""
"""
#find prime no in range:  #correct working
while True:
    us=int(input("Enter start no:- "))
    last=int(input("Enter last no:- "))
    for j in range(us,last+1):
        if us>1:
            for i in range(2,j):
                if j%i==0:
                    break 
            else:
                print(j,end=" ")
        


#To find 1st hcf and them by formula Lcm of 2 no:
while True:
    us=int(input("Enter value 1:-"))
    us1=int(input("Enter value 2:-"))
    ma=max(us,us1)
    mi=min(us,us1)
    for i in range(mi,1,-1):
        if ma%mi==0:
            print(print("hcf is ;- ",mi))
            LCM=(ma*mi)/mi
            print("LCM is:- ",LCM)
            break
            #prime no condition 
        elif ((ma%i==0) and (mi%i==0)):
                print("Hcf is :- ",i)
                LCM=(ma*mi)/i
                print("LCM is:- ",LCM)
                break
    else:
        print("HCF if 1")
        LCM=(ma*mi)
        print("LCM is:- ",LCM)

                


#HCF for three variables:
#not work concept of middle variable
while True:
    us=int(input("Enter value 1:- "))
    us1=int(input("Enter value 2:- "))
    us2=int(input("Enter value 3:- "))
    ma=max(us,us1,us2)
    mi=min(us,us1,us2)
    for i in range(mi,1,-1):
        if ma%mi==0:
            print(print("hcf is ;- ",mi))
            break
            #prime no condition 
        elif ((ma%i==0) and (mi%i==0)):
                print("Hcf is :- ",i)
                break
    else:
        print("HCF if 1")



#FAbonaci series:
us=int(input("Enter last digit:- "))
print("1")
for i in range(0,us):
    f=i+(i+1)
    print(f,end=" ")





#creata multiplication of any no:
us=eval(input("which table will you creat? "))
def mul(us):
        for j in range(1,11):
            print(us,"×", j," = ",j*us)
mul(us)


#To find factors of no:
while True:
    user_in=eval(input("Enter any:- "))
    for i in range(1,user_in+1):  #starting from 1 bc any thing divides 0 gets error!
        if i==user_in:
           print("and",user_in,"factors of this no are:- ")
        elif user_in%i==0:
            print(i," ",end=" ")
        

            

#suffel of alphabes: using whit out function of shuffel But problem is same index or word reapeat many time! 
#it is run at a null list!
import random 
list3=[1,22,3,4,5,6,7]
while True:
    list=[]
    list2=[]
    us=input("enter a word:- ")
    us1=len(us)
    for i in range(0,us1):
        list2.append(us[i])
        k=random.randint(0,us1-1)
        list.append(us[k])
    print("your list:- ",list2)
    print("shuffel list:- ", list) 


    
import random
l=[2,5,8,6,9,7]
random.shuffle(l)
print(l)



#Recursive function 
while True:
#i=0 
    m=int(input("fact"))
    for i in range(1,m):
        m=m*i
        print(m)
        



while True:
    us=int(input("Enter no:- "))
    def fact(us):
        for j in range(1,us):
            us=us*j
            print(us)




for j in range(0,8):
    if j>1:
       j=j+(j-3)
       print(j)
    else:
        print(j)


pre=0
ag=1
ago(pre+)




#decting double space:
while True:
    us=str(input("Enter string:- "))
    if "  " in us:
        print("Yes present at intex no:- ",us.index("  ") )
    else:
        print("NOT presen!")



#Removing Double ques in string 
while True:
    us=input("Enter your strung sentence:- ")
    if "  " in us:
      k=us.replace("  ",'')
      print(k)
    else:
       print(us)

    

#codes for multiple space may be single or not
while True:
    us=input("Enter your strung sentence:- ")
    if ("  " or " ") in us:
       k=(us.replace("  ","") and us.replace(" ",""))
       print(k)
    else:
       print(us)
   
 


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
"""


print(3//2)