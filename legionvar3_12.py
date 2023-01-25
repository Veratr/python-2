#вариант 3 задание 12
s = '0'+'2'*30+'4'*54+'6'*10
while '02' in s or '04' in s or '06' in s:
    if '02' in s:
        s=s.replace('02', '6404', 1)
    if '04' in s:
        s=s.replace('04', '2206', 1)
    if '06' in s:
        s=s.replace('06', '440', 1)
print(sum(map(int, s[:-1])))        

