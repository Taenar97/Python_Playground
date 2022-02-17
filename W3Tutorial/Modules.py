#modules = libraries

#mymodule.py
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#myprogram.py
import mymodule
import mymodule as mx #renaming
mymodule.greeting("Jonathan")

x = dir(mx) #lists all function & variable names of a module

from mymodule import person1 #Import a certain thing from the module