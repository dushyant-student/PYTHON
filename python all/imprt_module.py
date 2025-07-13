"""import module   #module is a liberery of python , in which function or codes is defined which is mad by us!

print(module.sum(2,2))
#print(module(sum(2,2)))      ×
#print(module sum(2,2))      ×
print(module.divide(20,5))    #each & every prog kai liya run hone per last mai none jaroore print hoga!
print(module.divide(0,20))
print(module.mult(15,12))


#IMPORT AS ALLIYAS!
import module as m

print(m.sum(2,2))
#print(module(sum(2,2)))      ×
#print(module sum(2,2))      ×
print(m.divide(20,5))    #each & every prog kai liya run hone per last mai none jaroore print hoga!
print(m.divide(0,20))
print(m.mult(15,12))"""



#2. method import modules  , which is used only for comes a single function!
from module import divide
print(divide(30,2))


from module import mult
print(mult(30,2))


#if you import all functions of module then use all funtions!
from module import *

print(sum(2,2))
#print(module(sum(2,2)))      ×
#print(module sum(2,2))      ×
print(divide(20,5))    #each & every prog kai liya run hone per last mai none jaroore print hoga!
print(divide(0,20))
print(mult(15,12))
