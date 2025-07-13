import time
import random
while True:
    p=["one upon a time","life is very difficult to live","this man is quinique","what was you thinking at this time","how are you","some of the story are very sad"]
    print(random.choice(p))
    start=time.time()
    us=str(input("Check typing skill: "))
    final=time.time()
    print("total time is:-",final-start)
    if len(us)==len(p):
        i=0
        for k in range(0,len(p)):  #this lop  only for when same leng of words are you wright len(p)==len(us) 
            if p[k]!=us[k]:
                i=i+1
                print(us[k],end=" ")
        print("total mistake is:- ",i)
    else:
        print("Please, Do all words are correct type!")
        choice=int(input("""Enter your choice1:-
                               1.continoue 
                                  2. EXITE!"""))
        