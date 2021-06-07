n, k, q = map(int, input().split())
arr = [int(i) for i in input().split()]
query = []
for i in range(q):
    query.append(int(input()))
arr = arr[-k%len(arr):] + arr[:-k%len(arr)]
for i in query:
    print(arr[i])
