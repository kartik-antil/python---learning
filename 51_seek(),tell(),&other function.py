
#seek()

with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(10)
    data=f.read(5)
    print(data) 

#tell()

with open('myfile.txt','r') as f:
    data=f.read(10)
    current_position=f.tell()
    f.seek(current_position)
    print(data)
    print(current_position)

#truncate()

with open('sample.txt','w') as f:
    f.write("hello kartik how are you")
    f.truncate(5)
with open('sample.txt','r') as f:
    print(f.read())

