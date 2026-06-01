l,b = map(int,input().split())
count = 0
while l <= b :
    count = count + 1
    l = 3 * l
    b = 2 * b
print(count)