def solve():
    safe=[0]*100
    m,x,y=map(int,input().split())
    arr=[int(i) for i in input().split()]
    for i in arr:
        min=i-x*y-1
        max=i+x*y-1
        if max>99:
            max=99
        if min<0:
            min=0
        for j in range(min,max+1):
            safe[j]=1
    print(safe.count(0))
t=int(input())
for _ in range(t):
    solve()
