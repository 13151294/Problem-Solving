a = str(input())
b = str(input())
Ascore = 0
Bscore = 0
a = [int(i) for i in a.split()]
b = [int(i) for i in b.split()]
for i in range(len(a)):
    if a[0] > b[0]:
        Ascore = Ascore + 1
    elif a[0] < b[0]:
        Bscore = Bscore + 1
    else:
        pass

print(Ascore, Bscore)