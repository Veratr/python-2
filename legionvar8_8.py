a = "KLMNO"
n = 0
for b in a:
    for c in a:
        for d in a:
            for e in a:
                for f in a:
                    w = b + c + d + e + f
                    if w[0]== "L" and (w[1]== "M" or w[2]== "M" or w[3]== "M" or w[4]=="M"):
                        if w[1] != w[2] and w[2] != w[0]:
                            if w[4] != w[3]:
                                print(w)
                                n+=1
print(n)
