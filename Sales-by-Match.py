n = int(input())
socks = list(map(int, input().split()))
socks.sort()
sockcolor = list(set(socks))
pair = 0
for i in range(len(sockcolor)):
    pair += socks.count(sockcolor[i]) // 2
print(pair)