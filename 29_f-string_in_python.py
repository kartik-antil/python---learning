#1. example

letter="hey my name is {} and i am from {}"
country="india"
name="kartik"
print(letter.format(name,country))

print(letter.format(country,name))

letter="hey my name is {1} and i am from {0}"
print(letter.format(country,name))

print(f"hey my name is {name} and i am from {country}")

#2.example 

txt="for only {price:.2f} dollars!"
print(txt.format(price=49.099999999))

price=49.09999
txt=f"for only {price:.2f} dollars"
print(txt)

#3.example

print(f"{2*30}")

print(type(f"{2*30}"))

#4.example

print(f"we use f-string like this: hey my name is {{name}} and i am from {{country}}")


