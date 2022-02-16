x = """Multi
Line
Strings
"""
#strings can be viewed as string arrays, though no datatype char exists -> string of length 1 instead
x = "Hello, World!"
y = x[5]

#looping through
for x in "banana":
    print(x)

#length
x = "Hello, World!"
print(len(x))

#check strings
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#slicing
x = "Hello, World!"
y = x[2:5]#character 5 is not included -> "llo"
z = x[:5]#-> "Hello"
a = x[2:]#-> "llo, World!""
b = x[-5:-2]#negativ indexing (starts from end) -> "orl"

#modifying
x = "Hello, World!"
y = x.upper()#Upper case
z = x.lower()#Lower case
a = x.strip()#Remove Whitespace before and after the text
b = x.replace("H", "J")#Replaces one string with another
c = x.split(",") # -> ['Hello', 'World!']
d = "Hello" + " " + "World!"#concatenation

#format
#Used for combining strings with non-strings
age = 36
txt = "My name is John, I am {}"
x = txt.format(age)#Takes unlimited arguments for the respective {}

txt = "I want to pay {2} dollars for {0} pieces of item {1}."#indexed placeholders
quantity = 3
itemno = 567
price = 49.95
y = txt.format(quantity, itemno, price)

#escape characters
txt = "We are the so-called \"Vikings\" from the north."
#\'         single qoute
#\\         backslash
#\n         new line
#\r         carriage return
#\t         tab
#\b         backspace
#\f         form feed
#\ooo       octal value
#\xhh       hex value

#methods
a = "Hello, World!"
a.capitalize()      #First char to upper case
a.casefold()        #String to lower case
a.center(20)        #Centers the string
a.count("l")        #Counts occurences of string
a.encode()          #encodes a string
a.endswith("!")     #true if string ends with string
a.expandtabs(2)     #sets the tab(\t) size
a.find("l")         #searches string for occurence of
a.format()
a.format_map()
a.index("wel")      #position of first occurence
a.isalnum()         #true if alphanumeric
a.isalpha()         #true if in alphabet
a.isdecimal()       #true if decimals
a.isdigit()         #true if digits
a.isidentifier()    #true if identifier
a.islower()         #true if all is lower case
a.isnumeric()       #true if all chars are numeric
a.isprintable()     #true if printable
a.isspace()         #true if all chars are whitespaces
a.istitle()         #true if string follows the rules of a title
a.isupper()         #true if all is upper case
a.join()            #joins all items of an iterable into one string
a.ljust()           #left justified string
a.lower()           #lower case
a.lstrip()          #left trim version
a.maketrans()       #translation table
a.partition("lo")   #parts the string into threee pieces
a.replace()
a.rfind()
a.rindex()
a.rjust()
a.rpartition()
a.rsplit()
a.rstrip()
a.split()           #splits string at sperator
a.splitlines()      #splits string at linebreaks
a.startswith()
a.strip()
a.swapcase()        #swaps cases
a.title()           #converts every first char of a word to upper case
a.translate()
a.upper()
a.zfill()           #fills with 0 chars from front