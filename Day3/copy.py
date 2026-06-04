n = int(input())
vote = list(map(int, input().split()))
age = list(map(int, input().split()))
c = [0] * max(vote)
for i in range(n):
    if age[i] >= 18 :
        c[vote[i]-1] += 1
print(c)

#5
#1 2 1 3 2
#17 21 20 19 18