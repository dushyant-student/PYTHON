# NESTED DICTINORY:-
#nested dict is combination of two or more dict's in a dict OR  it means putting dict inside another dict 
"""
f={'dushyant':{'age':9, 'a':6,'b':30},
   "sahu":{"age":10,'a':15,'b':25}}
print(f['dushyant']['b'])   #if we use double qute inside dushyant dont allowed!
for k,v in f.items():
    print(k,v['a'],v['b'])
    f["sahu"]['b']=30     #update value of dictonery:-
    print(k,v)




#TOUPLE() INTRODUTION :-
#imutable data type ,does not change its value ,order sequence data type print always same!
#touple doesnt allow single value !, s('p') type:-string  or s(5) type:- int , it is not touple it is string .
#workes on index no:-

t=("f","d",2,"%","+")
i=t[3]
#tuple itration
k=len(t)
for s in range(k):
    print(t[s] ,i)


#2.nd method for printing all elements in formate column:-
for a in t:   #same result as uper1
    print(a)

#function for tuple:-
j=("m",3,'l',6,8,0,"@","end")
k=(2,4,7,5,0,2)
min(k)
max(k)
#r=min(j)  #not support str & int:-
#r=max(j)
r=j.count(0)   #not correct r=count(3) ×
r=j.index(6)    #not correct r=index(4) ×
r=sum(k)  #not correct k.sum()
sum(k,3)
print(r,k)




#  sets{}:-set & dict have same symbole but set define only for values , unoderd , un index no, insert new data,but dont change previous touple ,  
#dont store same value in multiples times , o/p-- ramdom variable :-
# FUNCTIONS :- 
s={"4","g",9,"*",4,8}
s1={1,0,"g",3,2,"k",6,5,3}
d=["sum","j","3"]
#for a in s:  ,this funct is also applicable
#print(a)
d.clear()   #result o/p :-- set()
print(d)
set()
s.add("c")   #add new element 
s.pop()   #ramdom delet element 
s.remove("*")   #remove accor to you choice  #note :- if value is note present show error 
s1.discard("g")     # Element not in list don't show erreor 
print(s1)
s.update(d)   # show all element in new set with dict elememt ! ,without reapt element! 
print(s)
"""



















