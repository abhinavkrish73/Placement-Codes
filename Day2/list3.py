l1 = input().split()
l1.sort()
res = []
for i in l1:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)

#Print even numbers together in descending order and odd numbers in ascending order in the same list
# input -> 6 2 3 1 7 5
# output -> [6, 2, 1, 3, 5, 7]