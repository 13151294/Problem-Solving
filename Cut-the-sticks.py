n = input()
arr = [int(i) for i in input().split()]
while len(arr) > 0:
    print(len(arr))
    Least = min(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] - Least
    for i in range(arr.count(0)):
        arr.remove(0)
