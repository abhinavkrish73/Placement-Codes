def pp(n):
    print(n)
    if n == 2 :
        return 2
    else :
        pp(n-2)

pp(10)