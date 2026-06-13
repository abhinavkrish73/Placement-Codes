def pp(n):
    if n == 0 :
        print(200)
        return
    print(n)
    pp(n-1)
pp(5)