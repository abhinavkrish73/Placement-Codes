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
while n>0:
    dig = n%10
    rev=rev*10+dig
    n=n//10
while rev>0:
    dig=rev%10
    sum1 = sum1 + (dig ** count)
    count=count-1
    rev=rev//10
print(sum1)