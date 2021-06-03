def count(n, s, d, m):
    return sum([1 for i in range(n-m+1) if sum(s[i:i+m])==d])
n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())
print(count(n, s, d, m))