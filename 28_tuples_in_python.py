tup=(1,3,5)
print(type(tup),tup)

tup=(1)
print(type(tup),tup)

tup=(1,)
print(type(tup),tup)

tup=[1,2,56,78,94]
tup[0]=90
print(tup)

tup=[2,56,67,92,"red"]
print(tup)
print(tup[0])
print(tup[1])
print(tup[3])

if 34 in tup:
    print("yes it is present ")
else:
    print("no it is not present")
    # also slicing doing in tupple as well as lists 

#operation on tuples 
#manipulating tuples:
 
 #1. example
countries=("spain","india","italy","england","germany")
temp=list(countries)
temp.append("russia")
temp.pop(3) # it remove the index ( england)
temp[2]="finland"
countries=tuple(temp)
print(countries)

#2.example 
countries=("pakistan","afghanistan")
countries2=("vietnam","india","china")
southEastAsia=countries+countries2
print(southEastAsia)

#3. count() method
tuple=(0,1,2,3,3,2,1,1,1,5,6,1)
res=tuple.count(1)
print("count of 1 in tuple is :" , res)

#4. index() method
tuple=(0,1,2,3,4,5,6,2,3,3,3,3,4,5,6)
res=tuple.index(3)
print("count of 3 in tuple is :" ,res) # which position is on 3 is : output
res=len(tuple)
print(res)

