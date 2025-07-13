#simple pattern and single pattern:
"""
user_ip=int(int(input("Enter in put:- ")))
for i in range(0,user_ip+1):
    

#start double pattern 
    print("*" * i)
for k in range(user_ip,0,-1):
    print("*"*k)
    
    

#new symbole decreacing order :
ip=int(input("Enter input:- "))
for j in range(ip+1,1,-1):
    print("#" * j)
for s in range(1,ip+1):
    print("#" * s)
    
    
    
    
#symole increasing order by pattern,bas extra part gap hai jo dec order mai kernai hai :- 

ip=int(input("Enter input:- "))
const=ip
for j in range(ip,0,-1):
    print(" " * int(const-j),"*" * j)
for s in range(ip,0,-1):
    print(" " * s,"*" * int(const-s))
    
    


#remove same pattern single pattern is printing two times 
ip=int(input("Enter input:- "))
const=ip
for j in range(ip,0,-1):
    print(" " * int(const-j),"*" * j)
for s in range(ip-2,0,-1):
    print(" " * s,"*" * int(const-s))
    
#note yes it sussefull 




##square box pattern 
us=int(input("enter box no :- "))
print("*" * us)
const=us
for k in range(us,-1,-1):
    if k!=0:
        print("*" * 1," " * int(const-4) ,"*" * 1)
    elif(k==0):
        print("*" * us)
        
 



#making Box hahing same dimenstions len=breadth with same no of gaps 
#yes perfect work
du=int(input("ENter no:- "))
con=du
print(" *" * con)
for d in range(du,0,-1):
    if d==2:
        print(" *" * con)
    elif (d==(0 or 1)):
        break
    elif d!=2:
        print(" *" * 1,"  " * int(con-3) ," *" * 1 )
        
        
"""



#make a dimond by table of star

# us=int(input("enter a no :- "))
# print("*" * us)
# con=us
# mid=(us//2)+1
# for i in range(1,us+1):
#     if i<(mid):
#         print("*" * (mid-i)+" " * abs(int((2*i)-1))+"*" * (mid-i))
#     else:
#         break
# for k in range(1,mid-1):
#     print("*" * int(k+1)+" " * abs(int(2 *k)-int(us-2))+"*" * int(k+1))

#if we use this concept then one gap is exetra print and by this + helps removes gapes while commas generates extra gaps 

# print("*" * (mid-i),"e" * abs(int((2*i)-1)),"*" * (mid-i))

#x=2
# y=3
# p=input("ebddt:-")
# print()




def sum(arr,target):
    bs=[]
    j=0
    for i in range(0,len(arr)):
        if arr[i]+arr[j]==target:
            bs.append(i)
            bs.append(j)
            return bs
            
    j=j+i

arr=[2,7,11,15]
target=9
val=sum(arr,target)
print(val)


