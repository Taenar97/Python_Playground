#lists are ordered and changable. duplicate members are allowed (arrays)

x = ["apple", "banana", "cherry"]
y = len(x) #length of list
z = x.count("banana") #counts number of apperances

#Any datatype is supported
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#mixtures are allowed
list1 = ["abc", 34, True, 40, "male"]

#list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

#list access
x = ["apple", "banana", "cherry"]
y = x[0]    #first item
z = x[-1]   #last item
a = x[0:2]  #range of items
b = x[1:]
c = x[:2]
d = x[-1:-3]

#item check
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#item change
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[3] = ["watermelon"] #normal exchange
thislist[1:3] = ["blackcurrant", "watermelon"] #exchange items in range
thislist[1:2] = ["blackcurrant", "watermelon"] #exchange one item with two new ones
thislist[1:3] = ["watermelon"] #exchange two items with one
thislist.insert(2, "watermelon") #inserts a new item without changing others
thislist.append("orange") #appending at the end
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #append a whole list, tuple, set, dictionary,...
thislist.remove("banana") #remove specified item
thislist.pop(1) #removes item at index, last one if not specified
del thislist[0] #deletes item at index
del thislist #deletes whole list
thislist.clear() #empties whole list

#looping through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

[print(x) for x in thislist] #shorthand for-loop printing whole list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #list with only fruits with an a inside

#Sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #alos case sensitive
thislist.sort(reverse = True) #descending

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #sorting by custom function (how close to 50)

thislist.sort(key = str.lower) #to ignore case-sensitivenes

thislist.reverse() #reverses list with current order

#Copying a list
list1 = list2 #This only makes a reference to list1!!!

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #copies a list
mylist = list(thislist) #same result as copy

#Joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

for x in list2:
    list1.append(x)

list1.extend(list2)