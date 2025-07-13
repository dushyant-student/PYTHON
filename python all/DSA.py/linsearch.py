#Linear search without using function 
#WORKS CORRECT!
"""
list=[]
h=int(input("How many elements will you add ?:-", ))
for j in range(h):
 ui=int(input("Enter your elements:-",  ))
 list.append(ui)
print(list)
u=int(input('Enter your search no:-', ))
for j in range(h):
   if list[j]==u:
    print("your element present in list on index:-",j)
    break  
else:
   print("element not found:-",list)


   
   
#1.b:- soln 
list=[]
u=int(input('Enter how many no have you:-', ))
for i in range(u):
    q=int(input("enter no:-",  ))
    list.append(q)
print(list)
k=int(input('Enter element search in list:-', ))
if list[i]==k:
   print("Yes elem present ",k,"in list!","at index no:-",i)
else:
    print('this element not in list:-', )



   



#correct WORK! for using while loop!

#2nd method:-
list=[]
h=int(input("How many elements will you add ?:-", ))
for j in range(h):
   ui=int(input("Enter your elements:-",  ))
   list.append(ui)
print(list)
u=int(input("enter search ele:-",  ))
l=0
while l==len(list)-1:
   if list[l]==u:
     print("your element",u," present in list!","Index no:-",l)
   l=l+1
else:
   print("element not found:-",list)
 









#Works correct lineaar search
def linsea(list,u):
   for j in range(len(list)):
    if list[j]==u:
      print("your element present in list on index:-",j)
   
      break  
   else:
      print("element not found:-",list)
list=[1,88,34,9,7,6,62,67,6,55,5,67,9,48]
u=len(list)
linsea(list,67)
print("---------->")
print(linsea(list,9))   #why through at last (none)
"""