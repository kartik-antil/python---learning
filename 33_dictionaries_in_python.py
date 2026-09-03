dic={
    "kartik":"human being",
    "spoon":"object",
}
print(dic["kartik"])

info={"name":"kartik","age":19,"eligible":True}
print(info)
print(info["name"])
print(info["age"])
print(info["eligible"])
print(info.get("name"))
print(info.get("eligible"))

# ascessing multiple values from  a dictionary
info={"name":"kartik","age":19,"eligible":True}
print(info.keys())
print(info.values())
for key in info.keys():
    print(info[key])
    print(f"the value of corresponding to the key {key} is {info[key]}")


#  acessing key values pairs from a dictionary
info={"name":"kartik","age":19,"eligible":True}
print(info.items())
for  key, value in info.items():
    print(f"the value of coresponding to the key {key} is {value}")
