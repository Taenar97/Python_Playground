#Datatypes are asigned at creation, no explicit declarations
x = 3
y = "Sally" #It doesn't matter if single qoutes '' or double ""
z = 5.4
print(type(x))
print(type(y))
print(type(z))

#Casting is possible though
a = str(3)
b = int(3)
c = float(3)

#Variables are case-sensitive
a = 4
A = 'Sally'

#Multi-value assignment
x, y, z = "Orange", "Banana", "Cherry"


#Value assignment to multiple variables
x = y = z = "Orange"

#Value unpacking from collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

#Print statement
print("This is the variable z: " + z)

#Variable scope
global_var = 5;

def myfunc():
    #scope of local variable is only inside functions. If a variable is of the same name as a global,
    #only the local will be used/modifed
    local_var = 6

    #global keyword changes the scope
    global global_var_inside_function
    global_var_inside_function = 7
    
    #Can also be used to change a global variable inside a function
    global global_var
    global_var = 8;