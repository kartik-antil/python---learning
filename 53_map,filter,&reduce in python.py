#map
def cube(x):
    return x*x*x
print(cube)

l=[1,2,6,4,3]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl) 

l=[1,2,6,4,3]
newl=[]
for item in l:
    newl=list(map(cube,l))
print(newl) 

l=[1,2,6,4,3]
newl=[]
for item in l:
    newl=list(map(lambda x:x*x*x,l))
print(newl) 


#filter 
def filter_function(a):
    return a>4
newnewl=filter(filter_function,l)
print(newnewl)

def filter_function(a):
    return a>4

list(filter(filter_function,l))
print(newnewl)


#reduce()
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]
sum=reduce(lambda x,y : x+y,numbers)
print(sum)

def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)