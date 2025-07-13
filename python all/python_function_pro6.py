#FUNCTIONS IS BLOCK OF CODES WHICH PERFPORMS A SPECIFIC TASK!. WHICH IS USED BY CALLING HELP &  DOES NOT NEED TO AGAIN & AGAIN WRIITE 
#SAME CODES IT SAVES TIME OF DEVLOPERS
"""
def show():
    print("data")
show()


#2.function :-
def value(a,b):   #just like a user input!
    print(a+b)
    value(3,7)



#SIMPLE INTREST FORMULA 
def simple_int(p,r,t):
    print((p*r*t)/100)  #string is allow in under print !
simple_int(2,3,4)
simple_int(5,4,3)
simple_int(0,2,3)
#simple_int(s,p,l)    ×
#simple_int("s","p","k")  ×



#MULTIPLICATION NO :-
def sum(a,b,d):
    print("multiplycation is:_",a*b*d)
#    sum(2,3,4)  ,#NOTE:- doesn't show result if when we use undersore at calling function!
sum(2,3,4)
  

#SQUARE OF ANY NO:-
def square(s):
    print(s*s)
square(3)"""


#speed function :- using return function !
def speed(distance,time):
   # return"speed is:-" , distance/time ,"km\h"   #result,o/p:-- show with string 
 return " speed is:-", distance/time, "km\h"
   # return("speed is:-" , ,"km\h")  #in Bracket return is not allowed !
speed(10,2) #does not call only store value data.
s=speed(10,2)
print(s)



#SQUARE & sum OF ANY 2 diff NO  Using return statment:-
def square(s , p):
    return s*s , p*p
s=square(3,4)
print(s)





