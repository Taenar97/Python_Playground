#Naming conventions

#Variables, functions, methods, packages & modules:
lower_case_with_underscores = ...

#Classes & Exceptions:
UpperCaseWords

#protected methods & internal functions
_single_leading_underscore(self, ...)

#Private methods:
__double_leading_underscore(self, ...)

#Constants:
ALL_CAPS_WITH_UNDERSCORES

#Reverse notation:
elements = ...
elemnts_active = ...
elements_defunct = ...

#Imports:
import canteen
import canteen.sessions
from canteen import sessions

#Documentation:
""""Return the pathname of ``foo``."""

class Person(object):
    """A simple representation of a human beeing.
    :param name: A string, the person's name.
    :param age: An int, the person's age.
    """
    def __init__(self, name, age) :
        self.name = name
        self.age = age

#Try to avoid comments in exchange for code readability
#Line lenghts 80-100 chars
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore