# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 01:24:43 2026

@author: user
"""
# "This is HW 1 "

"""
Work submitted by Eric Steinfelds.
"""

# Task 1:  Variable Declaration and Data Types

variables= ["","",""]
variables= variables+[0]

variables[0]=8
variables[1]=31.14159/2
variables[2]= "thingString"
variables[3]= True

print("my integer is ",variables[0])
print("my real numb is",variables[1])
print("my charSting is ",variables[2])
print("my Boolean param is ",variables[3])

print("hi ___________________ ")

"  Task 2: String Manipulation "

WorExpression="Maplesoft_and_Python"
print( WorExpression.lower() )
print( WorExpression.upper() )

print( WorExpression.swapcase() )
print("test switching")
print( WorExpression.replace('a','o')     )
print( WorExpression.replace('Map','mmMAAP')     )

# the below seems useless
newStrin= WorExpression.split("_,_")
print( WorExpression.split("_,_") )
print(" ")

" Task 3: Basic Operations "
a , b, c = 11 , 22 , 33
# arithmetic
prodabc= (a+b)*2 + 1.2*(a+b)/(10+c*c)
print("(a+b)*2 + 1.2*(a+b)/(10+c*c) ==",prodabc)
print("Is it true that a < b ?? , Answer is ",a<b)
print("Is it true that 2*a == b ?? , Answer is ",2*a==b)
print("Is it true that a > c ??, Answer is ", a>c )
# Next I carry out some logic operation via Python
print("a< b OR a>b ", a<b or a>b)
print("a< b AND a>b ", a<b and a>b)
print(" I DENY that a > b. This denial is ", not (a>b) )

" Task 4: Data Collections "
"      Create examples of the following data structures:  "
""" o	List
	o  Dictionary
	o  Tuple
"""

mio_listo= [ 2, 3, 5, 7, 11 ]
Schh="Scythian"
mio_dictio= {"Name":"Anna","edad":23,"tribe":Schh}
mio_tuple= (13,17,19,23 )

# I refer to the index number as it is used in Maplesoft
#    But here I comply with index setting from 0 for Python
print("element sub 2 of list is ",mio_listo[2-1])
print("tribe_Name in mio_dictio is ",mio_dictio["tribe"] )
print("element sub 3 in the Tuple is ",mio_tuple[3-1])


" Task 5: Expression Combination "
"""
	Write a Python expression that combines multiple variables and 
             operations into a single meaningful expression.
"""
print( (a==b)*(a*a+b*b))
print( (a<b)*(a*a+b*b)  )
skvag= (float(a)+1/100 )**2 + (float(b)+1/100 )**2
print(int(skvag))
import numpy as np
leng_a_b=  np.sqrt(skvag)

print("sqrt(a^2+b^2) = ",leng_a_b,
      " is worth considering as this is greater than side 'a' ;",leng_a_b>a)

