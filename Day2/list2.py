l1 = input().split()
res = []
for i in l1:
    if l1.count(i) % 2 != 0 :
        if i not in res:
            res.append(i)
print(res)

# input -> 1 1 1 2 2 3 3 3
# output -> ['1', '3']
