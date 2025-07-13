#creat game to main tain file with highscore by user input!

HG=int(input("enter high score:-", ))
MS=50
with open("highscore.txt","w") as f:
    if HG>MS:
      f.write(str(HG))
if HG<MS:
     with open("highscore.txt","w") as t:
         t.write("50")



 