#max frequent element
l = [1,2,2,2,2,3,3,3,3,3,3,4,4]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else :
        d[i] += 1
max = 0
ans = 0
for i in d:
    if d[i] > max :
        max = d[i]
        ans = i
print(ans)