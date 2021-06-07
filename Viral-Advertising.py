Day = int(input())
receive = 5
Cumulative = 2
for i in range(Day-1):
    receive = receive // 2 * 3
    Cumulative += receive//2
print(Cumulative)
