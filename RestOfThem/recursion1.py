def pp(n):
    if n == 0 :
        return
    print(n)
    pp(n-1)
pp(5)
