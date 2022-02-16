#A set is unordered, unchangable (only the items) and unindexed
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
thisset.remove("banana") #can raise an error if item doesn't exists
thisset.discard("banana")#raises no errors
thisset.pop() #removes last item
thisset.clear() #empties the set
del thisset #deletes the whole set

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #adding another set

#Joining sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #new set with items from both sets
set1.update(set2) #inserts items from set2 into set1

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #keeps only the duplicates
z = x.intersection(y) #new list with only the duplicates
x.symmetric_difference_update(y) #keeping everything except the duplicates
z = x.symmetric_difference(y) #new list without the duplicates
x.difference_update(y) #removes items that exist in both sets
z = x.difference(y) #new list with items that only exist in x, and not in y
z = x.isdisjoint(y) #true if no items in set x is present in set y
z = x.issubset(y) #true if all items in x are present in y
z = x.issuperset(y) #true if all items in y are present in x
