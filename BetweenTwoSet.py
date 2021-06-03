input()#this is useless input
def Between2Set(lista, listb):
    count = 0
    for num in range(max(a), min(b) + 1):
        left = all([num % i == 0 for i in lista])
        right = all([j % num == 0 for j in listb])
        count += left*right
    return count
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(Between2Set(a,b))