#12.isalnum()
#A-Z , a-z , 0 to 9 
str1="welcometheconsole1"
print(str1.isalnum())

#13.isalpha()
#A-Z , a-z , not numbers
str1="welcome"
print(str1.isalpha())

#14.islower()
str1="hello world "
print(str1.islower())

#15.isprintable()
#printable chracter given true & imprintable given false 
str1="we wish you a Merry christmas "
print(str1.isprintable())

str2="we wish you a Merry christmas \n"
print(str2.isprintable())

#16.isspace()
str1="                      "  #using spacebar
print(str1.isspace())

str2="                      "  #using tab
print(str2.isspace())

#17.istitle()
#first word of each word of the string is capitalized else it return false
str1="World Health Organisation"
print(str1.istitle())

str2="To kill a Mocking bird"
print(str2.istitle())

#18.isupper()
str1="WORLD HEALTH ORGANIZATION"
print(str1.isupper())

#19.startswith()
str1="Python is an Intepreted language"
print(str1.startswith("Python"))

#20.swapcase()
#uppercase-lowercase , lowercase-uppercase
str1="Python Is An Intepreted Language"
print(str1.swapcase())

#21.title()
str1="His name is dan. Dan is an honest man"
print(str1.title())