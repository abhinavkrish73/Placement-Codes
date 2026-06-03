l = [2,3,4,3,3,5,4]
max = 0
for i in l:
    if i > max:
        max = i
l2=[]
max2=0
for i in l:
    if i > max2 and i != max:
        max2 = i
print(max2)