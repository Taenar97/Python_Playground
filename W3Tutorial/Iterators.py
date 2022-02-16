#An iterator is an object that contains a countable number of values
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which
#you can get an iterator from. Can be used in for loops.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#creating an iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

#Adding a termination to prevetn endless running
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20: #termination condition
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration #termination

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)