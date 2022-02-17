i = 1
while i < 6:
  print(i)
  i += 1

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break #break leaves the while loop
  i += 1 

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #skips the current iteraation and goes on with the next
  print(i)

#else block
i = 1
while i < 6:
  print(i)
  i += 1
else: #runs once after condition isn't true anymore
  print("i is no longer less than 6")