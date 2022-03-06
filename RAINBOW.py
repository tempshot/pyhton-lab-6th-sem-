for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=1
    p1,p2=0,n-1
    if arr[p1]!=1:
        flag=0
    else:
        while (p1<p2):
            if arr[p1]!=arr[p2]:
                flag=0
                break
            if (arr[p1]!=arr[p1+1]) and (arr[p1+1]!=arr[p1]+1):
                flag=0
                break
            p1 +=1
            p2 -=1
        if arr[p1]!=7:
            flag=0
    if flag==1:
        print("yes")
    else:
        print("no")
