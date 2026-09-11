import random
import string
st=input("enter message:")
coding=input("1 for coding or 0 for decoding:")   
coding=True if (coding=="1") else False
words=st.split("  ")

if coding:
    nwords=[]
    for word in words:
        if len(word)>=3:
            r1="".join(random.choices(string.ascii_letters,k=3))
            r2="".join(random.choices(string.ascii_letters,k=3))
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])    
        print("  ".join(nwords))
else:
    nwords=[]
    for word in words:
            if len(words)>3:
                stnew=word[3:-3]
                stnew=stnew[-1]+stnew[:-1]
                nwords.append(stnew)
            else:
                 nwords.append(word[::-1])
    print("  ".join(nwords))

 


        


