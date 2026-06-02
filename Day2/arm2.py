n=int(input())
count=0
n1=n
n2=n
sum1=0
rev=0
while n1>0:
    dig=n%10
    count=count+1
    n1=n1//10
while n2>0:
    dig=n2%10
    sum1 = sum1 + (dig ** count)
    count=count-1
    n2=n2//10
print(sum1)