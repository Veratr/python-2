print ("z, w, y, x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x== (not y)) <= (z ==( y or w))):
                    print (z, w, y, x)