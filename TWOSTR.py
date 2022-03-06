t=int(input())
for _ in range(t):
    a=input()
    b=input()
    ca=[]
    cb=[]
    c=0
    for i in a:
        ca.append(i)
    for i in b:
        cb.append(i)
    for i in range(len(ca)):
        if(ca[i]==cb[i] or ca[i]=='?' or cb[i]=='?'):
            c+=1
        else:
            c=0
            break
    if(c!=0):
        print("Yes")
    else:
        print("No")
