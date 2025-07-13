""" 21.  #string itration 
a='my name is bhoot'
c =len(a)
for s in range(1,c+1,2):  #diff in range() function boundery commas seprated and but indexing is X[2::1]
 print("the breaking string:- ",a[s])



#by using function for i in w:-
d="why is not cleaver man "

for i in d:
    print(i)




#by using function for i in w:-
d="why is not cleaver man "
for i in d:
    print(i[1::2])        #never work 



 #22. SOME FUNCTION of string :-
    # NOTE:- this is only valid on string case !  
  #  .capitalize :- sentances of first word of letter is captlize ( ex:- This is cat bright   )
   #   .upper  :-  complte sentances is captilise (EVERY WORD OF SENTENCE IS CAPTALISED  )
    #  .title  :-  every word of sentance first letter is big(ex:- The Sonu Is Old )
    #  .lower  :-  complete sentance is convert in small latter case(ex:- this is cat)

 #CODES:-

a="My namE is DusHyAnt "
s=a.capitalize()   #bracket is apply because it is function 
p=a.upper()
d=a.lower()
j=a.title()
print("ans",s,p,d,j) 



  #COMMON FUNCTIONS OF STRING :-
     #NOTE APPLY ON STRING CASE !
  #  .find(" ")  :- gives index no , if index is nt avaliable for that word return -1 !
  #   .index(" ") :- give index no , if any word have not index no Gives in error !
  #   .alpha()     :- return true only, when only letters are present in hole string !
  #    .isdigit()   :- returns true only when whole string only have counting no !
  #    .isalnum()    :- return ,at least one condition of (digit or letters or both ) is satisfy ! 



a="bfksjjjawgahce"
s=a.find("s")
p="bfksjjj6246291awgahce"
b="bfksjjja7857wgahce"


print(a.find("s"),"=", s,"(both will be same)" , a.index("e") , a.isalpha() , p.isdigit() , b.isalnum() )
print(a.find("a" ,9) , a.index("z"))  # 9 kai baad dhund daiga is k matlab hai!
                        # if by index no is not in this string gives error! 




#24.  function 
 #chr()  :- i/p numbers --> o/p letter 
  ===> both are depends on snall later and capatlale letter!
 #ord()  :- i/p letter --> o/p number 

#CODES:-
##chr()
s=chr(99)  ==> type string !
 #p=chr(105,100,100)   #show type error only we can take only one argument! 
print(s,chr(100) ,"p" )

## ord()  #note :- cant never takes multiples value in bracket ex:- s=("P","e")this is incorrect !
d=ord("g" )  
b="j"          #always variables in string otherwise show not defined !
print(d,ord(b),type(d))   #--> type is integer ! 




#28. list comprehension :-
#list comprehension is generlly is more compect and fast than normals function and loop !
for i in range (101):                                           #list
    p=[]                                                     #   [1]
    p.append(i)     #hundred list is made in column patten   #   [2]
    print(p)                                                 #   [3]
                                                                
  #@                                                              
t=[]
for j in range(101):  #o/p--> [1,2,3,4,5,......]
 t.append(j)
print(t)



#comperehesion use :- 
s=[m for m in range(1,101) ]

p=[h for h in range(101) if h%2==0]  #we can pass any condition without any comma !
print(p,s)   #two list sre created same as case #@


#this comprehension function used for also strnig !
#ex;- 
w="my name is dushynt"
j=len(w)
print(j)
z=[j for j in range(j) if int(j)%2==0] 
print(z)
   

 #29. functions NOTE :- not apply on list !
 #  .pop  :-
 #   .delete()  :- 
 #    .clear( blank)
 #     .remove(excat no)
 #      .append(list)
 #       .extend(list)
    

l=[2,3,4,56,7]
print(l)  #o/p --> [2,3,4,7]

print(q.pop(4))  #show pop element(7) and o/p--> [2,3,4,7]
print(l)     # pop works on index value



#print(l,remove(56)) # ×
#c=l.remove(56) 
q.remove(56)
print(l)   #REmove excate value(56) ==o/p --> [2,3,4] correct list!

l.clear()   #do blanck full list [---]
 
l.insert(1,30)   #l.insert(index no , element pass) ==> insert on any position  element on basics of index !
print(l)

n=[1,3,2]
l.append(n)  # append element at last  or anywhere found , possible to add substrings !
print(l)  #o/p-->[2,30,3,4,[1,2,3]] give sub list !


l.extend(n)
print(l)    #o/p--> [2,30,4,1,2,3] give continous list !



#30. NOTE:- 
#function apply. on list only.   #can check method of repersent

t=[1,"l",3,2,2,1,"k",53,435,3,"j",21,1,23,4,6]
print(t.count(2))


s=max(t) #give max vlue of counting or abcd
print(s)


f=min(t)  #give min va;ue 
print(f)

t.sort()
print(t)  #arrange inscreasing order 

t.reverse()
print(t)  #decreasing order 


print(t.index("j"))#gives index no  #firmate --> .index(value,start point ) 
      
 #take excate value get index daigaa no. bass difreence yai find and index mai ki .index gives  an error if word is not avilable in string
"""


#WHILE TRUE CONDITION    ( %%%%%%%%%%%%%%%)                          #GIVEN WHILE TRUE 

while True:
 a=int(input("enter numbers when till is not end pro"))
 if a==5:      #pro continouous  run again and again with run program      # CONDITION FOR STOPE PROGRAM 
   break 

















