import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #Searches if the String starts with 'The' and ends with 'Spain'

#Findall function -> List containing all matches
x = re.findall("ai", txt)

#Search function -> Match object (only first occurence) or None
x = re.search("\s", txt)
print(x.start())

#Split function -> List with split up String
re.split("\s", txt)
re.split("\s", txt, 1) #maximun number of splits

#Sub function -> replaces text
re.sub("\s", "9", txt)
re.sub("\s", "9", txt, 2) #number of replacements

#Match object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object 
print(x.span()) #tuple containing start and end positions of match
print(x.string) #string passed into the function
print(x.group()) #part of the string where there was a match

#Metacharacters
x = "[a-m]"         #A set of characters
x = "\d"            #a special sequence or escape special chars
x = "he..o"         #Any character except newline
x = "^hello"        #starts with
x = "planet$"       #ends with
x = "he.*o"         #zero or more occurences
x = "he.+o"         #one or more occurences
x = "he.?o"         #zero or one occurences
x = "he.{2}o"       #excatly the specified number of occurences
x = "falls|stays"   #either or
x = "()"            #capture and group

#Sets
x = "[arn]"         #match if a, r or n are present
x = "[a-n]"         #match for any lower case character between a and n
x = "[^arn]"        #match for any character except a, r and n
x = "[0123]"        #match if 0, 1, 2 or 3 are present
x = "[0-9]"         #match if 0-9 are present
x = "[0-5][0-9]"    #match for any two digit numbers from 00 to 59
x = "[a-zA-Z]"      #match for any lower and upper case character
x = "[+]"           #+,*,.,|,(),$,{} have no special meaning in sets, so match if + char is present

#Special sequences (\ + following)
x = "\AThe"         #match if specified chars are at the beginning of string
x = r"\bain"        #match where specified chars at the beginning of a word. r is for raw string treatment
x = r"ain\b"        #match where specified chars at the end of a word
x = r"\Bain"        #match where chars are present, but not at beginning of word
x = r"ain\B"        #match where chars are present, but not at end of word
x = "\d"            #match where string contains digits
x = "\D"            #match where string does not contain digits
x = "\s"            #match where string contains a whitespace
x = "\S"            #match where string does not contain a whitespace
x = "\w"            #match where string contains any word (0-9, a-Z, _)
x = "\W"            #match where string does not contain any word (0-9, a-Z, _)
x = "Spain\Z"       #match if specified characters are at the end of string