import json

#JSON to Python
#some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse the JSON object:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Python to JSON
#Python dictionary
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON object:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Convertible are:
#dict, list, tuple, string, int, float, True, False, None
#Objects will be converted to JSON equivalent:
#Object, Array, Array, String, Number, Number, true, false, null
json.dumps({"name": "John", "age": 30})
json.dumps(["apple", "bananas"])
json.dumps(("apple", "bananas"))
json.dumps("hello")
json.dumps(42)
json.dumps(31.76)
json.dumps(True)
json.dumps(False)
json.dumps(None)

#Results can be formated for better readablility
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json.dumps(x, indent=4) #define indents
json.dumps(x, indent=4, separators=(". ", " = ")) #changing default seperators
json.dumps(x, indent=4, sort_keys=True) #Sort the parameters
