#Tuples are ordered and unchangable, duplicates are allowed
thistuple = ("apple", "banana", "cherry")

#tuples with only one item have to have a , or they willl not be coorect
thistuple = ("apple",)

#changing is not possible but can be made with a work around (tuple -> list -> tuple)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

#adding tuples is allowed
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

#unpacking tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #the * makes the last item a list if there are too much tuple
(green, *tropic, red) = fruits #add as much items to the second until only one is left for the last

#multiplying tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2