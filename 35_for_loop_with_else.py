#1. example of for loop with else statement
for i in  range (5):
    print(i)
else:
    print("sorry no i is here")

#2. example of for loop with else statement
"""
for i in range():
    print(i)
else:
    print("sorry no i is here")
"""
    # this show error

#3. example of for loop with else statement
for i in range(6):
    print(i)
    if i==4:
         break
else:
    print("sorry no i is here")

#4. example of for loop with else statement
i=0
while i<7:
    print(i)
    i=i+1
else:
    print("sorry no i is here")

#5. example of for loop with else statement
i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("sorry no i is here")

#6. example of for loop with else statement
for x in range(5):
    print("iteration no. {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")