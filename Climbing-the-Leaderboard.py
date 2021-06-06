input()
Leaderboard_Base = sorted(list(set(map(int, input().split()))))
input()
User_Score = sorted(list(map(int, input().split())))
index = 0
n = len(Leaderboard_Base)
for i in User_Score:
    while (n > index and i >= Leaderboard_Base[index]):
        index += 1
    print(n+1-index)
