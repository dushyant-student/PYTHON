l=[]
while True:
    c=int(input(""" 1. encue the ele?
                    2. Decue the ele?
                    3. front ele?   
                    4. rear ele? 
                     5. exit----> """))
    if c==1:
        us=int(input("enter your ele:-"))
        l.append(us)
        print(l)
    elif c==2:
      if len(l)==0:
        print("your Que is empty")
      else: 
        del l[0]
        print("your que after deque",l )
    elif c==3:
       print("front element", l[0])
    elif c==4:
       e=len(l)-1
       print("last(rear) ele:-",l[e])
    elif c==5:
        break


    




