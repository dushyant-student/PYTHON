i=100
def reverse():
    global i
    i=i-1
    print(i)
    if i!=0: 
       reverse()
reverse()
