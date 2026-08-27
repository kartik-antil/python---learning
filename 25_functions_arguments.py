#default arguments
#1.example 
def Average (a, b):
    print("the average is ",(a + b)/2)
Average (6,3)

#2.example
def Average (a=87,b=65):
    print("the average is ",(a+b)/2)
Average()

#3.example
def Average (a=45,b=73): #python ignores the default values if we pass the values in the function call  
    print("the average is ",(a+b)/2)
Average(34,89) #python accepts the values passed in the function call and ignores the default values

#4.example
def name(fname,mname,lname):
    print("hello",fname,mname,lname)
name("kartik","antil","sachdeva")

#required arguments
def Average (a,b,c=1):
    print("the average is ",(a+b+c)/2)
Average(7,5)

#keyword arbitary arguments
#1.example
def Average (*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is :",sum/len(numbers))
Average(6,8,2,2,7)

#2.example
def name(**name):
    print("hello",name["fname"],name["mname"],name["lname"])
name(fname="kartik",mname="antil",lname="sachdeva")

#return statement
def Average(*numbers):
    sum=0
    for i in numbers :
        sum=sum+i
    return sum/len(numbers)
c=Average(7,9,5,4,9)
print(c)
