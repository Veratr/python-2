world = "ЕДОНК"
n = 0
for a in world:
    for b in world:
        for c in world:
            for d in world:
                w = a + b + c + d
                if w.count("О") ==2:
                    print(w)
                    n+=1
print(n)

