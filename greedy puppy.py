t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    max = 0
    for j in range(1,k+1):
        r=n%j
        if r>max:
            max=r
    print(max)
