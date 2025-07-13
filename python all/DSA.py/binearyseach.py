#it is working working!
"""list=[]
h=int(input("How many elements will you add ?:-", ))
for j in range(h):
   ui=int(input("Enter your elements:-",  ))
   list.append(ui)
list.sort()
print(list)
e=int(input("enter search ele:-", ))
l=0
u=h-1
k=0
while l<=u:
     k=(l+u)//2
     if list[k]==e:
        print("Yes your ele is in list,At index no:-",k)  #use print statment only one time 
        break
     elif list[k]<e: 
        l=k+1
     elif list[l]>e:
        u=k-1
else:
     print("your ele is not present in list!")

   
"""


#this correct working 
u=[2,4,9,10,14,33,37,41,55,60,69,137,238,359,378,430,476,576,656,666,876]
#List must be shorted!  
print(len(u))
k=0
l=21    #len(u)-1
n=int(input('enter search no:-', ))
mid=0
while k<=l:
  mid=(k+l)//2
  if u[mid]==n:
    print('Yes, this element is present:- Index no=',mid)
    break
  elif u[mid]<n:
    k=mid+1
  elif u[mid]>n:
    l=mid-1
else:
  print('ele not found!')






#this bineary search not work!
def bin(u,n=9):
   l=0
   mid=0
   k=9
   while l<=k:
     mid=(l+k)//2
   if u[mid]==n:
     return mid 
     print('Yes, this element is present:- Index no=',mid)
   elif (u[mid]<n):
     l=mid+1
   else:
     return mid-1
   return -1
#print('ele not found!')
u=[2,4,9,10,14,33,37,41,55]
bin(u,9)

