x =5**200+25**1000-5**50
s = ''
while x != 0: 
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count("0"))
