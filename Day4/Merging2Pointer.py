l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
i = 0
j = 0
res= []
while i < len(l1) and j < len(l2):
    if l1[i]<l2[j]:
        res.append(l1[i])
        i=i+1
    else:
        res.append(l2[j])
        j=j+1
while i < len(l1):
    res.append(l1[i])
    i=i+1
while j < len(l2):
    res.append(l2[j])
    j=j+1
print(res)