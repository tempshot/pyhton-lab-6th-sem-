actual=input()
t=int(input())
for i in range(t):
    
    test=input()
    ind=0
    for i in test:
        
        if i not in actual:
            print("No")
            ind=1
            break
    if ind==0:
        print("Yes")
