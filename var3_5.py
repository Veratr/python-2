colvo=0
for n in range(1, 1000):
    r= bin(n)[2:] #bin переводит из десятичной в двоичную
    if r.count('1') % 2==0: #.count считает количество каких-либо знанков в переменной(в данном случае 1)
       r=str(r)+'00' #str - стороковый тип данных. + складывание строк
    else:
        r=str(r)+"10"
    if r.count('1')%2==0:
        r=str(r)+'0'
    else:
        r=str(r)+'1'
    if int(r, 2)>130 and int(r, 2)<350:
        colvo+=1
print(colvo)