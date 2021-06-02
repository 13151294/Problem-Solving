x1, v1, x2, v2 = (int(i) for i in input().split())
if ((x2 - x1) * (v2 - v1) < 0) and ((x2 - x1) % (v2 - v1) == 0):
    print("YES")
else:
    print("NO")