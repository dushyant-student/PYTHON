"""def inser(arr,index,insertele):    #WHY is not working?
    for i in range(len(arr)-1,-index+1,1):
        arr[i]=arr[i-1]
    print(arr) 
    arr[index]=insertele
    print(arr) 
arr=[12,18,37,9,28,49,69,37,83]
inser(arr,3,99)
print(arr)    #this not work due to list range index cant expend after posted list!
"""




#Insertion OF ARRAY ELEMENT IS CORRECT!
def dep(arr,ind,val):
   for j in range(len(arr),ind,-1):
     arr[j-1]=arr[j]
     arr[ind]=val
arr=[18,55,57,46,97,2,8,34,99,468,48,25,1]
dep(arr,3,303)
print("--------->")
dep(arr,5,33)
print(arr)

