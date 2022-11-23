print("z, y, x, w")
for z in range(2):
    for y in range(2):
        for x in range(2):
            for w in range(2):
                if not((((not z) and y) <= x) and (x <=(not y))):
                    print(z, y, x, w)