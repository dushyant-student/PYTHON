
"""#04.

#IF WE USE IF & IF AGAIN &  again STATMENT then at a time previous condion is run again and again!    

print("hello world")  #print sucessfully

print(23)  #asume as a integer value 
#But code doesn't run when sum of any number with help of maths opperaters ex:-
print('2+3')  #does not show the sum of any nums its just like as a string 

print(2+2)  #yes show sum of numbers ans:- 4

print(10>2)   #o/p show only in form of true or false ans:- yes 




#VARIABLE 
'''RULE:-  1. start variable is not is counting no ex:-
  wrong method is that :- 1a ,a b ,@a ,61& ,3# ,$# a=3 
   
WRIGHT method id a1 ,ab ,a ,_a, a_b ,'''

a=12  # Here a,b,c are variable and we store some data like string(" ") , values( 2,3,4,7,9), character( a,y,t,r,h),list,
#touple ,dictionery and can store special chracter 
#like( @ ,# ,$ ,&) ,
#string is a text which we want run any word as it print
b=23
c=26
d=23
print(a,b , "c ")  #o/p 12  23  c , c is under in double quatation is string 

  

   #FUNCTION ID :- SHOW MEMORY LOCATION OF  OUR DATA WHICH IS ASSIGN IN VARIABLE EX

print(id(b)+ id(d)) # print b d with memory location , in differ variable but value is same then memory location is same 


# SRING CONCATENATE:- SYNBOL (+) # role adding two or more string ,words and sum of two numbers 
e="self"
f="name "
print(e+f)  #show o/p:- selfname if we want to print space b/w
print(e+" "+f)
#show o/p:- selfe name
#if will do print(a+b)  #show sum of number:- 37

print(a+33)  #show sum of num 45
#print(a+e)  #show error because different data type set by you int + string dont add it always same types of data type is concatinate 


#7. operators 
1. Arithmetic operator:- cal +, -,/ division  ,**exponentes/power   , //floor division ,* multiplication , modulus %(gives rem vale in int)
 2. assignment operator:- = , += ,-=
 3. comparision operator:- <,>,<= ,>=
 4. logical operator:- or ,and , not etc
 5. identity operator:- is ,is no #REturns only ans in true or false.
 6 membership operators:- in , not in. #REturns ans only in true or false  
 7. Bitwise operator:- A&B (returns true only when both is true ) 
 *.  A|B (or oper returs if atleast one is true returns true )
 *.  A^B returns fale if both is same """



#DATA TYPES:- 
""" MUTABLES:- (change its state and values,contents ) ex:- list[] , dictonary{ 'a' : 'b'} ,bytes array
List is an orderd sequenc of character items or value and flexible datatype,list is slow than tuple.
Tuple is orderd sequence of items () ,tuple is fast accessable than dictonary ,touple have always min at least one value
otherwise that is not touple.

IMUTABLES:- (cant change is states and values,contents ) ex:- tuple , string, int ,float ,complex, tuple ,set """
 

#TYPE CASTING with user input functions:- input(
# int() handel only int value
# float() haldle only point values 
# eval () Handle all types of value ex:_ int,float,i/p binery digits gives o/p int )
#calculator"""


"""#######RANGE FUNCTION:-
for i in range(start,end(n-1), increament):  #loop follow for increasing order , n= any no given by you
for i in range(greatest no , -infinity , -decrement value):  #loop folow decreasing order



#CREATING A TABLE OF 5 :-

for i in range(1,11):
  print("5 × ",i ,"=", i*5)



  #CREAT TABLE OF ANY NUMBER WITH USER UINPUT:-
 
a=eval(input("enter your number:- ", ))
for i in range(1,11):
  print(a ," × ",i ,"=", i*a)  


  #CREAT A LIST AND ASIGN A NEW VARIABLE:-
l=[1,2,3,"s","B","$","@"]
l[3]="%"      # if we put khali l[3]=%  without putting (" " )show error
print(l,type(l))
  


#WHILE LOOP FUNCTION:- 
i=2 
while i<=10:
  print(i,"stop!")
  i=i+1
  
  
  

#WHILE LOOP FUNCTION in decing order :- 
i=12
while i>=7:
  print(i,"stop!")   #LEARN THIS SEQUENCE 
  i=i-1


#COUNTING THE STRING:-
a="the no of words this sentence "
b=len(a)  
for g in range(b):       
 #print("sclicing of this string is:- ",g ) 
    #or
 print("stope!",a[g])


#INDEXING AND SCLICING:-
D="MY NAME IS INDEXING "
c=len(D)
for i in range(c):
 print(D[i])

 #method 2 
D="MY NAME IS INDEXING "
print(D[0:6]) # o/p my Nam
print(D[-1:-6]) #not show result
print(D[-2:-8:-2]) #o/p:- GIE
"""



\
  