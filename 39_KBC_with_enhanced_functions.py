questions= [
    ["which language was used to create facebook?","python","french","javascript","php","none",4],
    ["which language was used to create instagram?","python","french","javascript","php","none",4],
    ["which language was used to create youtube?","python","french","javascript","php","none",4],
    ["which language was used to create whatsapp?","python","french","javascript","php","none",4],
    ["which language was used to create twitter?","python","french","javascript","php","none",4],
    ["which language was used to create telegram?","python","french","javascript","php","none",4],
    ["which language was used to create terabox?","python","french","javascript","php","none",4],
    ["which language was used to create spotify?","python","french","javascript","php","none",4],
    ["which language was used to create snapchat?","python","french","javascript","php","none",4],
    ["which language was used to create messenger?","python","french","javascript","php","none",4],
    ["which language was used to create yt music?","python","french","javascripts","php","none",4],
    ["which language was used to create linkedin ?","python","french","javascripts","php","none",4],
    ["which language was used to create  fiverr?","python","french","javascripts","php","none",4],
    ["which language was used to create github?","python","french","javascripts","php","none",4],
    ["which language was used to create upwork?","python","french","javascripts","php","none",4],

]

levels=[1000,2000,3000,4000,8000,16000,32000,64000,100000,320000,1000000,5000000,10000000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nquestion for rs. {levels[i]}")
    print(f"a.{question[1]}               b.{question[1]}")
    print(f"c.{question[3]}               d.{question[4]}")

    reply=int(input("enter your answer(1-4) or 0 to quit:\n"))

    if reply==0:
        money=levels[i-1]
        break
    if reply==question[-1]:
        print(f"correct answer, you have won rs.{levels[i]}")
        if i==4:
            money=10000
        elif i==9:
            money=320000
        elif i==14:
            money=10000000
    else:
        print("wrong answer")
        break
print("your take home is {money}")