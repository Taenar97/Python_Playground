try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Another exception has occured!")

#else block -> will be executed if no error occurs
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#finally block -> will be executed regardless of error or not
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close() #cleans up wether writitng was succesefull or not
except:
    print("Something went wrong when opening the file")

#Raising exceptions
x = -1
if x < 0:
    raise Exception("No numbers belwo zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")