list=[]
u=int(input('enter no of ele:-', ))
for i in range(u):
    e=int(input('enter elem:-', ))
    list.append(e)
print(list)
d=int(input('enter elem insert:-', ))
p=int(input('index no:-', ))
l=len(list)
for k in range(p,l-1):
 list[k]=list[k+1]
list[p]=d
print(list)
      
#fun se chl raha hain

   





