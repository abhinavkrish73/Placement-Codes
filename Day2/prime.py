n = int(input())
flag=0
if n==1 or n==0 :
    print("Neither Prime or Composite")
    exit(0)
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        flag=1
        break
if flag==0:
    print("Prime")
else:
    print("Composite")