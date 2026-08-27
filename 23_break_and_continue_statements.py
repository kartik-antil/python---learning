#break statements
for i in range(12):
    if(i==10):
        break
    print("5 X",i+1,"=",5*(i+1))
print("loop end")

#continue statements:
for i in range(12):
    if(i==10):
        print("skip the itreation")
        continue
    print("5 X",i,"=",5*i)
        
# do while loop emulate:
i=0
while True:
    print(i)
    i=i+1
    if(i%10==0):
        break
