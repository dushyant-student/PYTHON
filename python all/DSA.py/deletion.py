#def dele(arr,ind,val):
arr=[3,44,2,65,182,9,38,45,5,55,4,45,8,54,4,95,456,78]
k=len(arr)
ind=int(input("enter value:-",  ))
arr.pop(ind)
for i in range(len(arr)-1,ind,-1):
  arr[i]=arr[i-1 ]  
#del(arr,3,99)
print(arr,k,len(arr))

