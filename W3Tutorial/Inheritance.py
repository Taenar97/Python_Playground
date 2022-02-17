#Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#Child class
class Student(Person):
    def __init__(self, fname, lname, year): #overrides the parents function
        Person.__init__(self, fname, lname) #calls parents function
        super().__init__(fname, lname) #inherits all methods and properties from parent
        self.graduationyear = year #adds a new propertie
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()