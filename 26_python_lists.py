#1.example
l=[3,4,6]
print(l)
print(type(l))
print(type(0))
print(type(1))
print(type(2))

#2.example
l=[3,5,8,"kartik","True"]
print(l)

#3.example
marks=[3,5,6,8,9,2,7]
print(marks[-6])
print(marks[len(marks)-6])
print(marks[7-6])
print(marks[1])

#4.example
marks=[3,5,7,9,2]
if 8 in marks:
    print("yes")
else:
    print("no")

print(marks[:])
print(marks[1:-1])
print(marks[1:4:2])