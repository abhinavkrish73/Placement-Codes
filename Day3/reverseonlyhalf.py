l = [1,2,3,4,5,6,7,8]
fa = 0
la = len(l)//2 - 1
temp = 0
for i in range(len(l)//4):
    temp = l[fa]
    l[fa] = l[la]
    l[la] = temp
    fa+=1
    la-=1
print(l)
