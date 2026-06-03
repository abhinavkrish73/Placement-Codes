n = int(input())
vote = list(map(int, input().split()))
age = list(map(int, input().split()))
d = {}
for i in range(n):
    if age[i] >= 18 :
        if vote[i] not in d :
            d[vote[i]] = 1
        else :
            d[vote[i]] += 1
print(d)
max = 0
for i in d :
    if d[i] > max :
        max = d[i]
        ans = i
        count = 1
    elif d[i] == max :
        count += 1
if count > 1 :
    print(-1)
else : 
    print(ans)
