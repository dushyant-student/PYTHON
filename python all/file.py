us=int(input("Enter score:- "))
g=open('remove2.txt','r')
if int(g)<us:
    j=g.write(us)
    print(j)
else:
    print(g)
g.close()

