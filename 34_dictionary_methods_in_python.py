# it is ordered 
#1. update()
employees={122:67,123:45,675:78,546:36}
employees2={222:67,566:90}
employees.update(employees2)
print(employees)

#2. clear()
employees={122:67,123:45,675:78,546:36}
employees2={222:67,566:90}
employees.clear()
print(employees)

#3. pop()
employees={122:67,123:45,675:78,546:36}
employees2={222:67,566:90}
employees.pop(122)
print(employees)

#4. popitem()
employees={122:67,123:45,675:78,546:36}
employees2={222:67,566:90}
employees.popitem()
print(employees)

#5. del
employees={122:67,123:45,675:78,546:36}
employees2={222:67,566:90}
del employees[122]
print(employees)


