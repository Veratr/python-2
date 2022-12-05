a = {0: "Е",
      1: "К",
      2: "О",
      3: "Р"}
k = 0
for i in range (0,len(a)):
    for j in range (0,len(a)):
        for b in range(0, len(a)):
            for c in range(0, len(a)):
                for d in range(0, len(a)):
                    for v in range(0, len(a)):
                        k +=1
                        world = str(k) + "К" + a[i] + a[j] + a[b] + a[c] + a[d] + a[v]
                        print(world)
#ответ:3822  

