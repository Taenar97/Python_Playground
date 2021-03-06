from sympy import true


a = "Hello World"                               #str
b = 20                                          #int
c = 20.5                                        #float
d = 1j                                          #complex
e = ["apple", "banana", "cherry"]               #list
f = ("apple", "banana", "cherry")               #tuple
g = range(6)                                    #range
h = {"name" : "John", "age" : 36}               #dict
i = {"apple", "banana", "cherry"}               #set
j = frozenset({"apple", "banana", "cherry"})    #frozenset
k = true                                        #bool
l = b"Hello"                                    #bytes
m = bytearray(5)                                #bytearray
n = memoryview(bytes(5))                        #memoryview

#Explicit declaration can be used (casting)
x = str("Hello world") #Same for all datatypes

#Random numbers
import random
x = random.randrange(1, 10)