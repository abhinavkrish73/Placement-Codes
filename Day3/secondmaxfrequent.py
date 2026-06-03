#Second highest frequent element
l = [1,2,2,2,2,3,3,3,3,3,3,4,4]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else :
        d[i] += 1
max = 0
ans = 0
max2 = 0
ans2 = 0
for i in d:
    if d[i] > max :
        max2 = max
        ans2 = ans
        max = d[i]
        ans = i
    elif d[i]>max2 and d[i]!=max :
        max2 = d[i]
        ans2 = i
print(ans2)