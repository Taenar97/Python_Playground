x, y = 5

#arithmetic
x + y   #addition
x - y   #subtraction
x * y   #multiplication
x / y   #division
x % y   #modulus/ rest
x ** y  #exponentiation
x // y  #floor division/div

#assignments
a = x
a += x
a -= x
a *= x
a /= x
a %= x
a //= x
a **= x
a &= x  #a = a & x
a |= x  #a = a | x
a ^= x
a >>= x #a = a >> x
a <<= x #a = a << x

#comparison
x == y  #equal
x != y  #not equal
x > y   #greater 
y < y   #smaler
x >= y  #greater or equal
x <= y  #smaller or equal

#logical
x < 5 and x < 10
x < 5 or x < 10
not(x < 5 or x < 10)

#identity
x is y      #true if the same
x is not y  #true if not the same

#memebership
x in y      #true if x is in y
x not in y

#bitwise
x & y       #AND
x | y       #OR
x ^ y       #XOR
~x          #NOT
x << y      #Zero fill left shift
x >> y      #Signed right shift