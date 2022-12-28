x =125**300 * 5**300 - 25**70 - 100
s = ''
while x != 0: 
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count("4"))