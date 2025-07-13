def stack(arr):
    while True:
        r=len(arr)
        c=int(input("""what do you want with arry:-
                          1.encue ele
                          2. decue ele:-
                          3. show front ele:-
                          4.  show rear ele:-
                               5. EXIT! 
                    ENTER YOUR CHOICE?"""))
        if c==1:
            if r==6:
                print('your stack is full!')
            else:
                g=int(input('enter your ele:- '))
                arr.append(g)
                print(arr)
        elif c==2:
            if r==0:
                print("""stack is empty you can'ydelete ele?""")
            else:
                arr.pop(-1)
                print(arr)
        elif c==3:
            print("front ele is:-",arr[r-1])
        elif c==4:
            print("Rear ele is:-",arr[0])
        else:
            break
print(stack([1,2,3,4,5,6]))



#fun using return statment 

def stack(arr):
    while True:
        r=len(arr)
        c=int(input("""what do you want with arry:-
                          1.encue ele
                          2. decue ele:-
                          3. show front ele:-
                          4.  show rear ele:-
                               5. EXIT! """))
        if c==1:
            if r==6:
                return ('your stack is full!')
            else:
                g=int(input('enter your ele:- '))
                arr.append(g)
                return (arr)
        elif c==2:
            if r==0:
                print("""stack is empty you can'ydelete ele?""")
            else:
                arr.pop(-1)
                return (arr)
        elif c==3:
            print("front ele is:-",arr[r-1])
        elif c==4:
                return ("Rear ele is:-",arr[0])
        else:
            break
print(stack([1,2,3,4,5,6]))


