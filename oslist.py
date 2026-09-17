import os 
folders=os.listdir("data")
print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


import os 
folders=os.listdir("data")
print(os.getcwd())
os.chdir("/users")
print(os.getcwd())