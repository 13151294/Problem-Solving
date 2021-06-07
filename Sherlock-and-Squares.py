from math import floor, sqrt

for i in range(int(input())):
    Start, Stop = map(int, input().split())
    print(floor(sqrt(Stop)) - floor(sqrt(Start-1)))
