a=input("enter a number:")
print(f"multiplication table of {a} is :")
for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")

a=input("enter a number:")
print(f" multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("invalid input")
print("some imp lines of code")
print("end of program")

try:
    num=int(input("enter a number:"))
    print(f"multiplication table of {num} is :")
    for i in range(1,11):
        print(f"{num} X {i} ={num*i}")
except ValueError:
    print("number entered is not valid")


#specific exception handling
try:
    num=int(input("enter a number:"))
    a=[3,8]
    print(a[num])
except ValueError:
    print("number entered is not valid")
except IndexError:
    print("index error")