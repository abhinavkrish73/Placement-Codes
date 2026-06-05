#rightRotation
l = list(map(int,input().split()))
n = len(l)
k = int(input())
k=k%n
l = l[-k:] + l[:-k]
print(l)