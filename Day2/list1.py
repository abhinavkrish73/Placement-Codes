l1 = input().split()
res = []
for i in l1:
    if i not in res:
        res.append(i)
print(res)

# input -> 1 1 1 1 6 6 6 6 3 3 3 3 
# output -> ['1', '6', '3']