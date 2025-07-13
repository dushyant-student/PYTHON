#code is perfectly work
print("Matrix 1:-")
arr=[[1,2,3],[4,5,6],[0,2,3]]
arr2=[[3,2,5],[6,3,5],[2,1,0]]
for arr3 in arr:
    print(arr3)
print("Matrix 2:- ")
for arr4 in arr2:
    print(arr4)

print("solution:-")
lst=[]
for g in range(0,3):
    col_lst=[]
    for i in range(0,3): #main concept is that loop is must run but not taking participate in quistion 
        ans =0
        for j in range(0,3):
            ans =ans +(arr[g][j]*arr2[j][i])
        col_lst.append(ans)
    lst.append(col_lst)
for res in lst:
    print(res)
