n = int(input("Enter size of list: "))
l = []
print("Enter elements: ")
for i in range(1,n+1):
    m = int(input())
    l.append(m)
print("Max element is: ", max(l))
