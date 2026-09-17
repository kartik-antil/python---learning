def double(x):
    return x*2

double=lambda x:x*3
print(double(6))

cube=lambda x:x*x*x
print(cube(4))

avg=lambda x,y:(x+y)/2
print(avg(4,8))

def appl(fx,value):
    return 6+fx(value)

print(appl(cube,6))
print(appl(lambda x:x*x*x,6))
lambda x,y:print(f'{x}*{y}={x*y}')


