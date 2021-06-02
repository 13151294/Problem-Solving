n = int(input())
for i in range(1):
    lists=[int(i) for i in input().split()]
    p = 0
    ng = 0
    z = 0
    for i in range(n):
        a = lists[i]
        if ( a > 0 ):
            p += 1
        elif ( a < 0 ):
            ng += 1
        else:
            z += 1
    porpoP = p / n
    porpoN = ng / n
    porpoZ = z / n
print(porpoP)
print(porpoN)
print(porpoZ)