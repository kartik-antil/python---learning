#strings are immutable
#strings cannot change 

#1.upper()
a="kartik"
print(len(a))
print(a.upper())

#2.lower()
a="Kartik Antil"
print(a.lower())

#3.rstrip()
a="Kartik !!!!!!!!"
print(a.rstrip("!"))

a1="!!!!!!Kartik!!!!!!"
print(a.rstrip("!"))
#it only remove back trailing chracter

#4.replace()
a="!!!!!kartik antil python!!!!!!"
print(a.replace("antil","do"))

#5.split()
a="!!!!!!kartik   !!!!   antil    !!!!    "
print(a.split(     ))

#6.capitalize()
heading="intoduction to js and python "
print(heading.capitalize())

#7.center()
str1="welcome to the console!!!"
print(str1.center(100))

str2="welcome to the console!!!"
print(len(str2.center(100)))
print(len(str2))

#8.count()
print(a.count("kartik"))

#you will get a boolean (True/False) amswer

#9.endswith()
str1="welcome to the console !!!!!!"
print(str1.endswith("!!!!"))

str2="welcome to the console!!!"
print(str2.endswith("to,4,10"))

#10.find()
str1="his name is dan. he is an honest man."
print(str1.find("is"))
print(str1.find("ishh"))

#11.index()
#value error if substring not found 
print(str1.index("dan"))

