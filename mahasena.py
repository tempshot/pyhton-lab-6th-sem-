size = int(input())
lis = list(map(int, input().split()))
e = 0
o = 0
for j in lis:
    if(j % 2 == 0):
        e = e+1
    else:
        o = o+1
if (e>o):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
