from typing import Iterator
def fibonacci(n:int)-> Iterator[int]:
    """ generate the first n fibonacci numbers efficiently."""
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
if __name__ == "__main__":
    print(*fibonacci(10))
