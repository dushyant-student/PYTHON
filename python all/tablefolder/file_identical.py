with open("remove.txt","r") as p:
    r=p.read()
    with open("remove2.txt",'r') as g:
       m= g.read()
    if r==m:
     print("both file is same! ")
    else:
     print("both files is not same ")
