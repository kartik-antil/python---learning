import time
hour_str= time.strftime("%H")
min_str=time.strftime("%M")
hour=int(hour_str)
print(f"current time is {hour_str} : {min_str}")
if(0<=hour<12):
    print("Good Morning Sir")
elif(12<=hour<16):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")