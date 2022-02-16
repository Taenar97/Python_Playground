#Dictionaries are ordered, changable and do not allow duplicates
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"] #accessing through key name
x = thisdict.get("model") #same result
x = thisdict.keys() #get list of keys
x = thisdict.values() #get list of values
x = thisdict.items() #get list of tuples

#looping through key value pairs
for x, y in thisdict.items():
    print(x, y)