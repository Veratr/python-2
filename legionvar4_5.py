colvo=0
for n in range(1, 1000):
    n2=bin(n)[2:]
    if n2[-1]==0:
        n2=n2+'00'
    else:
        n2=n2+'10'
    if n2.count('1')%2==0:
        n2=n2+'0'
    else:
        n2=n2+'1'
    r=int(n2, 2)
    if r>160 and r<630:
        colvo+=1
print(colvo)        
        
        