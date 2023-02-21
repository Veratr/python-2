for n in range(1, 1000):
    n2=bin(n)[2:]
    if n2.count('1')%2==0:
        n2= n2+'01'
    else:
        n2='1'+n2+'10'
    r=int(n2, 2)
    if r<105:
        print(n)