#KBC KAUN BANEGA CROREPATI
print("welcome to the KBC , the incribdle show presented by kartik")
name=input("enter your name:")
print("GREAT!!")

print("so your first question is :\nwho is the prime minister of india?")
lst1=["A. Narendra Modi","B.Yadav kalu","C.Rahul Gandhi","D.Jawaharlal Nehru"]
for option in lst1:
    print(option)

ans1=input("enter your answer:")
if ans1=="a" or ans1=="A":
    print("answer is right, you won 1,00,000 rupees")
else:
    print("lost,you are out of game")
    exit()


print("now, the second question is : \nwhat is the capital of india?")
lst2=["A.Amritsar","B.New Delhi","C.Haryana","D.Rajasthan"]
for option in lst2:
    print(option)
ans2=input("enter your answer:")
if ans2=="b" or ans2=="B":
    print("fantastic,your answer is correct you won 5,00,000 rupees")
else:
    print("you lost")
print("game over")


      