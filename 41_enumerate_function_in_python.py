marks=[12,56,32,98,12,45,1,4]
for mark in marks:
    print(mark)

marks=[12,56,32,98,12,45,1,4]
index=0
for mark in marks:
    print(mark)
    if index==3:
        print("kartik,awesome")
    index+=1

marks=[12,56,32,98,12,45,1,4]
for index, mark in enumerate(marks):
    print(mark)
    if index==3:
        print("kartik,great")

fruits=['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(index,fruit)

fruits=['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(f"{index+1}:{fruit}")

fruits=['apple','banana','mango']
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)