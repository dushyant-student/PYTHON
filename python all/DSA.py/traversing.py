def trav(arr):
    for i in range(len(arr)):
      print(arr[i])
arr=[11,18,19,34,29,7,281,18,1,15,46,4,4,64,645,5,77,55,5]
trav(arr)
print('------------>')
print(trav(arr))   #get none at last!



#Traversing array by user input without using function!
list=[]
us=int(input('Enter no of inputs will you enter?:-', ))
for l in range(us):
   ip=int(input('Enter no:-',  ))
   list.append(ip)
print(list)
for j in range(len(list)):
   print(list[j])




