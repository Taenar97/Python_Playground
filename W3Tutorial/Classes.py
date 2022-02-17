#blueprint for objects

#simple
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# __init__() function
#Every class has an init which is called by initiation/ object creation
class Person:
  def __init__(self, name, age):#self referes to the current object instance. Can be any word
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#methods in objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 
p1.age = 40 #propertie modification
del p1.name #delete propertie

del p1 #delete object

#pass statement
class Person:
  pass
