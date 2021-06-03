n = int(input())
lists = list(map(int, input().split()))
amount = [lists.count(i) for i in range(1,6)]
print(amount.index(max(amount))+1)