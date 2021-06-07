Start, End, Divisor = map(int, input().split())
Beautiful = 0
for day in range(Start, End+1):
    if (((day - int(str(day)[::-1])) / Divisor) % 1 == 0):
        Beautiful += 1
print(Beautiful)
