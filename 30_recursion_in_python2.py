#recursion is the process of defining something in term of itself
#factorial(7)= 7*6*5*4*3*2*1
#factorial(0)= 1
#factorial(n)=n*factorial(n-1)
#7!=7*(7-1)!

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)

"""
f(0)=0
f(1)=1
f(2)=f(1)+f(0)
f(n)=f(n-1)+f(n-2)
"""
# def fibonacci

def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#write a program to print fibonacci sequence

#1. example

n=int(input("please input any no. :"))
def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1 
    else:
        return f(n-1)+f(n-2)
print(f(n))

#2 . example 

from typing import Iterator
def fibonacci(n:int)-> Iterator[int]:
    """ generate the first n fibonacci numbers efficiently."""
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
if __name__ == "__main__":
    print(*fibonacci(10))



