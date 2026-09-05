"""
a=int(input("enter any value between 5 and 9 :"))
if (a<5 or a>9):
    raise ValueError("value should be between 5 and 9")
    """

user_input=input("enter no. between 5 and 9 (or type ' quite' to quit):")
if user_input.lower()=="quite":
    print(f"you type {user_input} so you are quite")

else:
    try:
        num=int(user_input)
        if num<5 or num>9:
            raise ValueError("value should be between 5 and 9")
    except Exception as e:
        print("error",e)
    else:
        print(f"you entered {num}")
print("program successfully completed")

