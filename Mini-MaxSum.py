lists = [0]
sumlist = []
sum = 0
lists.extend([int(i) for i in input().split()])
n = len(lists)
for i in range(n):
    sum += lists[i]
for x in range(1,n):
    no = 0
    no = sum - lists[x]
    sumlist.append(no)
print(min(sumlist), max(sumlist))