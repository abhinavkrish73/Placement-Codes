l = [1,2,3,4,5,6,7]
k = int(input())
for i in range(k):
    f = l[0]
    for j in range(0,len(l)-1):
        l[j]=l[j+1]
    l[len(l)-1] = f
print(l)