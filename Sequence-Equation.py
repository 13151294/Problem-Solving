n = int(input())
arr = [int(i) for i in input().split()]
sortArr = sorted(arr)
IndexArr = [arr.index(i)+1 for i in sortArr]
newArr = [IndexArr[sortArr.index(i)] for i in IndexArr]
print('\n'.join(map(str, newArr)))
