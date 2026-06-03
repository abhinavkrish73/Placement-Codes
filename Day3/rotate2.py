#rightRotation
l = [1,2,3,4,5,6,7]
k = int(input())
for i in range(k):
    la = l[len(l)-1]
    for j in range(len(l)-1,0,-1):
        l[j]=l[j-1]
    l[0] = la
print(l)