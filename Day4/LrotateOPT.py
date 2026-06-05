#leftRotation
l = list(map(int,input().split()))
n = len(l)
k = int(input())
k=k%n
l = l[:k][::-1] + l[k:][::-1]
l = l[::-1]
print(l)