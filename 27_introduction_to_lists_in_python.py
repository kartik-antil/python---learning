#list comprehension
l=[i for i in range(4)]
print(4)
l1=[i*i for i in  range(4)]
print(l1)
l2=[i*i for i in range (10) if i%2==0]
print(l2)

#list method
#1.append()
l=[1,2,4,6]
print(l)
l.append(7)
print(l)

#2 list.sort
l=[11,34,56,74,89]
print(l)
l.sort(reverse=True)
print(l)

l.sort()
print(l)

#3 list.reverse
l=[1,2,3,4,5]
l.reverse()
print(l)

#4 index()
l=[1,2,3,4,5,6,7,8,9]
l.index(1)
print(l)

#5 count()
l=[1,2,3,4,5,6,7,8,7,7,9]
print(l.count(7))

#6 copy()
m=l
m[0]=0
print(l)

m=l.copy()
m[0]=0
print(l)

#7. insert()
l.insert(1,788)
print(l)

#8. extend()
m=[900,1000,1100]
l.extend(m)
print(l)

k=l+m
print(k)