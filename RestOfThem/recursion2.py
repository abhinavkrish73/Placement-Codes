def pp(n):
    if n == 0 :
        return
    pp(n-1)
    print(n)
pp(5)
