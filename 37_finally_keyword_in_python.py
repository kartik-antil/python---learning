#finally clause
'''
finally clause Python mein exception handling ka ek crucial part hai. 
Iska sabse main feature ye hai ki iske andar likha hua code hamesha execute hota 
chahe:try block bina kisi error ke successfully run ho jaye.
except block kisi error ko catch (handle) kare.
Ya fir koi aisa unhandled error aaye jiski wajah se program crash hone wala ho.
'''
try:
    l=[1,5,6,7]
    i=int(input("enter the index:"))
    print(l[i])
except:
    print("some error occurred ")   
finally:
    print("i am always executed")



def func1():
    try:
        l=[1,5,6,7]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("i am always executed")
x=func1()
print(x)
