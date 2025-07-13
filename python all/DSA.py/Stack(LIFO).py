stack=[99,8,4,33,8,6]
while True:
    g=len(stack)
    c=int(input("""enter stack ele:-
                1. push ele
                2. delete ele
                3. show front ele 
                4. show rear ele 
                5. Exit """, ))
    if c==1:
        if g==6:
            print("stack is full not push ele:-",stack)
        elif g!=6: 
            f=int(input('enter your no:-'))
            stack.append(f)
            print('stack after deletion:-',stack)
    elif c==2:
        if g>0:
          stack.pop(-1)
          print(stack)
        if g==0:
           print('your stack is empty not del ele:-',stack)
    elif c==3:
        print(stack[0])
    elif c==4:
        print(stack[g-1])
    elif c>=15:
        break 







   

    

     