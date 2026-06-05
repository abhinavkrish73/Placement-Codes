l = list(map(int, input().split()))
k = int(input())
s,maxs=0,0
for i in range(len(l)-k+1):
    w = l[i:i+3]
    s=0
    for i in w:
        s = s+i
    if s>maxs :
        maxs = s
        w1=w[:]
print(maxs)
print(w1)