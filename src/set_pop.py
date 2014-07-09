'''
Created on Jul 9, 2014

@author: viejoemer

HowTo remove an arbitrary element and retrieve that item at the same time?

¿Cómo eliminar un elemento de forma arbitraria y recuperar ese elemento 
al mismo tiempo?

pop()
Remove and return an arbitrary element from the set. Raises KeyError
if the set is empty.
'''

#Create a set with values.
s_1 = set([1,2,3])
print("set one", s_1)

s_2 = set()
print("set one", s_2)

#Removing a element 
value = s_1.pop()
print("Element removed",s_1)
print("Value removed",value)

#If the set is empty return an error
value = s_2.pop()