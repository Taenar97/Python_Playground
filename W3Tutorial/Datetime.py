import datetime

x = datetime.datetime.now() #current date -> 2022-02-16 16:38:57.676123
print(x)

print(x.year) #year
print(x.strftime("%A")) #name of weekday

#creating date objects
x = datetime.datetime(2020, 5, 17)

#strftime() method. Takes an format argument
x.strftime("%a")    #Weekday short -> Wed
x.strftime("%A")    #Weekday full -> Wednesday
x.strftime("%w")    #Weekday number 0 - 6, 0 is sunday
x.strftime("%d")    #Day of month 01-31
x.strftime("%b")    #Month short -> Dec
x.strftime("%B")    #Month full -> December
x.strftime("%m")    #Month number 01-12
x.strftime("%y")    #Year short, no century -> 18
x.strftime("%Y")    #Year full -> 2018
x.strftime("%H")    #Hour 00-23
x.strftime("%I")    #Hour 00-12
x.strftime("%p")    #AM/PM
x.strftime("%M")    #Minute 00-59
x.strftime("%S")    #Second 00-59
x.strftime("%f")    #Microsecond 000000-999999
x.strftime("%z")    #UTC offset -> +0100
x.strftime("%Z")    #Timezone -> CST
x.strftime("%j")    #Day of year 001-366
x.strftime("%U")    #Week number of year 00-53, sunday as first day
x.strftime("%W")    #Week number of year 00-53, monday as first day
x.strftime("%c")    #local version of date and time
x.strftime("%C")    #century
x.strftime("%x")    #local version of date
x.strftime("%X")    #local version of time
x.strftime("%%")    #a % character
x.strftime("%G")    #ISO 8601 year
x.strftime("%u")    #ISO 8601 weekday 1-7
x.strftime("%V")    #ISO 8601 weeknumber 01-53