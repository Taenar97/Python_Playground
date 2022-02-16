#Lambdas are small anonymous functions with multiple arguments, but only one expression
x = lambda a : a + 10 #one argument
print(x(5))

x = lambda a, b : a * b #two arguments
print(x(5, 6))

x = lambda a, b, c : a + b + c #three arguments
print(x(5, 6, 2))

#power of lambdas
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))