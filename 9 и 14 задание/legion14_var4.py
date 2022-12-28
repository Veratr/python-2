for x in range (1, 10000):
    f = 81**8 + 3**7-9- x
    k  = 0
    while f > 0 :
        if f%3 == 2:
            k += 1
        f = f//3
    if k == 30:
        print(x)
        break
