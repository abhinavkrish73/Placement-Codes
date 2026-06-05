l = list(map(int, input().split()))
k = int(input())
s=sum(l[:k])
maxs = s
for i in range(1,len(l)-k+1):
    s = s - l[i-1] + l[i+k-1]
    maxs = max(maxs,s)
print(maxs)

