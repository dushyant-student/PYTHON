import random
while True:
    p=random.randrange(0,11)
    us=int(input("Enter your assum no range b/w -1 to 5:-"))
    if int(us)!=int(p):
        if us!=0 and p/us==2:
            print('''Your no is double the comp n
                     You are just near comp no:-'''
                    ,"your no:-",us,"& comp no:-",p)
            us=int(input("Enter no:-"))
            print("""your no is match to comp no!, 
                     You WON the Match""",p,"==", us)
        else:
           print("zero division error:-")
    if p!=0 and us/p==2:
        print("your no is just half the comp no, Your no ",us,"& comp no is:-",p)
        us=int(input("Enter your aprox no:-"))  
        print("""your no is match to comp no!, 
                     You WON the Match""",p,"==", us)
        if p!=0 and p/us==1:
           print("""your no is match to comp no!, 
                     You WON the Match""",p,"==", us)
        else:
            print("zero divison no:-")
    else:
        print("""Ypour no is greater than range!
                  try again selsct another no:-""")





    