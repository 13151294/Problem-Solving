d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())
if (d2>=d1 and m2>=m1 and y2>=y1) or (m2>m1 and y2>=y1) or (y2>y1):
    late=0
elif d2<d1 and m2==m1 and y2>=y1:
    late=15*abs(d2-d1)
elif m2<m1 and y2==y1:
    late=500*abs(m2-m1)
else:
    late=10000
print((late))
