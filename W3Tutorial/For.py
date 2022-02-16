#for is more like an iterator method than a classical for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in fruits:
  if x == "banana":
    break
  print(x)

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range() function
for x in range(6):#values 0 to 5
  print(x)

for x in range(2, 6):#values 2 to 5
  print(x)

for x in range(2, 30, 3):#values 2 to 29 with increments of 3
  print(x)

#else
for x in range(6):
  print(x)
else: #executes after loop is finished, but not if a break is applied
  print("Finally finished!")

#nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) 

#pass statement
for x in [0, 1, 2]:
  pass