x=4
print(x)
def hello():
    x=5
    print(f"the local x is{x}")
    print(x)

    print("hello world")

    print(f"the global x is{x}")
    hello()



x=10
def my_function():
    y=5
    print(y)
my_function()
print(x)



x=10
def my_function():
    global x
    x=4
    y=5
    print(y)
my_function()
print(x)