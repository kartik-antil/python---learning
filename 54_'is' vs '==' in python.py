a=4
b="4"
print(a is b ) # exact location of object in memory 
print(a==b) # value

a=[1,2,56]
b=[1,2,56]
print(a is b)
print(a==b)

a=3
b=3
print(a is b)
print(a==b)

a=7
b="kartik"
print(a is b)
print(a==b)

a="kartik"
b='kartik'
print(a is b)
print(a==b)

a="kartik"
b="python"
print(a is b)
print(a==b)