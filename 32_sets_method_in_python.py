#1 union() and update() method in python
s={1,2,5,6}
s2={3,6,7}
print(s.union(s2))

s={1,2,5,6}
s2={3,6,7}
print(s.update(s2))
print(s,s2)

cities={"tokyo","delhi","madrid","berlin"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.union(cities2)
print(cities3)

#2 intersection() and intersection_update() method in python
cities={"tokyo","delhi","madrid","berlin"}
cities2={"tokyo","seoul","kabul","madrid"}
cities.intersection(cities2)
cities.intersection_update(cities2)
print(cities)

#order does not matter 
#3 symmetric_difference() and symmetric_difference_update() method in python
cities={"tokyo","delhi","madrid","berlin"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.symmetric_difference(cities2)
cities3=cities.symmetric_difference_update(cities2)
print(cities3)

 #4 difference() and difference_update() method in python
cities={"tokyo","delhi","madrid","berlin"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.difference(cities2)
print(cities3)

#several in built methods 

# 1. isdisjoint()  which has no common elements
cities={"tokyo","delhi","madrid","berlin"}
cities2={"tokyo","seoul","kabul","madrid"}
print(cities.isdisjoint(cities2))

cities={"tokyo1","delhi","madrid2","berlin"}
cities2={"tokyo","seoul","kabul","madrid"}
print(cities.isdisjoint(cities2))

#2. issuperset() 
cities={"tokyo","delhi","madrid","berlin"}
cities2={"seoul","kabul"}
print(cities.issuperset(cities2))

#3. issubset()
cities={"tokyo","delhi","madrid","berlin"}
cities2={"delhi","madrid"}
print(cities.issubset(cities2))
print(cities2.issubset(cities))

#4. add()
cities={"tokyo","delhi","madrid","berlin"}
cities.add("helsinki")
print(cities)

#5. update()cities={"tokyo","delhi","madrid","berlin"}
cities={"tokyo","delhi","madrid","berlin"}
cities2={"helsinki","warsow","helsinki"}
cities.update(cities2)
print(cities)

#6. remove() and discard()
cities={"tokyo","delhi","madrid","berlin"}
cities.remove("tokyo")
print(cities)

#7. pop()
cities={"tokyo","delhi","madrid","berlin"}
cities.pop()
print(cities)

#8. del  it is a keyword not a method 
"""
cities={"tokyo","delhi","madrid","berlin"}
del cities
print(cities)
"""
  #this will give an error because cities is deleted
# so we can use comments the line to avoid error


#9. clear()
cities={"tokyo","delhi","madrid","berlin"}
cities.clear()
print(cities)

# check if items exists in a set 
# you can also check if an items exists in a set or not
info={"carla",19,False,5.9,19}
if "carla" in info:
    print("carla is present in the set")
else:
    print("carla is not present in the set")





