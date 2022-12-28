x = 256**500 * 4**100 - 64**30 - 8
s = ''
while x != 0: 
    s += str(x % 4)
    x //= 4
s = s[::-1]
print(s.count("3"))