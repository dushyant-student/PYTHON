"""def rough():
   name=[]
u=int(input('enter no of ele:-', ))
for i in range(u):
    e=str(input('enter elem:-', ))
    name.append(e)
print(name)
rough()
"""

"""
#INPUT FUNCTION CANT NEVER USE IN PTHON!
list=[]
u=int(input('enter no of ele:-', ))
for i in range(u):
    e=int(input('enter elem:-', ))
    list.append(e)
print("user list:-",list)
def selection(list):
    for i in range(1,len(list)):
        k=0
        for j in range(1,len(list)):
            if list[k]>list[j]:
                list[k],list[j]=list[j],list[k]
            k=k+1
selection(list)
print("sorted list:-",list)


#my code using function:
def sel(ar):
    for i in range(len(ar)-1):
        k=0
        for j in range(1,len(ar)):
            if ar[k]>ar[j]:
                ar[k],ar[j]=ar[j],ar[k]
            k=k+1
ar=[8,25,52,30,11,21,9,33,2,99,12,64,37,18,25,46]
sel(ar)
print(ar)







list=[]
man=int(input('enter elem:-', ))
list.append(man)
pv=list
nh=print(pv)
print(nh)
"""

""""
#INPUT FUNCTION CANT NEVER USE IN PTHON!
def selection(u):  
list=[]
for i in range(u):
    e=str(input('enter elem:-', ))
    list.append(e)
print("user list:-",list)
for i in range(1,len(list)):
        k=0
        for j in range(1,len(list)):
            if list[k]>list[j]:
                list[k],list[j]=list[j],list[k]
            k=k+1
selection(3)
print("sorted list:-",list)
"""
"""i=0
while i<=10:
    print(i)
    i=i+1


list=[1,2,3,4,5,6,7,8,9,10,9,9]
l=0
while l<=10:
   if list[l]==9:
    print(list)
    print(len(list),l)
print(l)
l=l+1
"""





"""
list=[1,2,3,4,5,6,7,8,9,9,10]
l=0
count=0
while l<10:
   if list[l]==9:
    count=count+1
    print(list,count)
l=l+1



##experiment for return statment 
def spd(l):
    while True:
        c=int(input('enter no:-'))
        if c==1:
           return ("first")
        elif c==2:
            return ("second")
        elif c==3:
            p=int(input('enter your no:-'))
            l.append(p)
            return l
        else:
            break
print(spd([1,2,3,4]))   
"""  
"""


def fun():
    e=int(input('enter a no:-'))
if e==3:
    def tum():
      'naeme'
    print(tum())
elif e==2:
       print("false")
else:
    print('none')
print(fun())
"""
    







