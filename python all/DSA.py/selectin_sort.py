''''def cell(list):
 list=[]
us=int(input("How many ele wil you enter:-", ))
for k in range(len(us)):
    b=int(input("Enter your ele:-", ))
    list.append(b)
jp=list
def cell(jp):
  k=0
for j in range(len(list)-1):
    k=j
    for l in range(1,len(list)):
       if list[l]<list[k]:
        k=l
    list[l],list[k]=list[k],list[l]
list=[1,8,28,12,25,67,138,175,64,575,4,5,78,7,45,257]
cell(list,)
print(list)  '''  



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




"""


#WEBsite ONLINE CODE:
def Selection_Sort(array):
    for i in range(0, len(array) - 1):
        s= i
        for j in range(1, len(array)):
            if array[j] < array[s]:
                s=j
        array[i], array[s] = array[s], array[i]

array = input('Enter the list of numbers: ').split()
array = [int(x) for x in array]
Selection_Sort(array)
print('List after sorting is : ', end='')
print(array)















def selectionSort(array, size):
    
    for ind in range(size):
        m= ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)"""