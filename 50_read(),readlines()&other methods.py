#readlines() method 

f=open('myfile.txt','r')
i=0
while True:
    line=f.readline()
    
    if not line:
        print(line,type(line))
        break
    line=line.strip()
    if not line:
        continue

    if "," not in line:
        continue

    i=i+1

    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i} in maths is: {m1}")
    print(f"marks of student {i} in english is: {m2}")
    print(f"marks of student {i} in science is: {m3}")

f.close() 


#writelines()method:

f=open('myfile.txt','w')
lines=['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()


