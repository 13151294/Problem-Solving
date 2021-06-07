Result = []
for i in range(int(input())):
    Input = input()
    Count = 0 
    for i in Input:
        num = int(Input)
        i = int(i)
        if i > 0 and num / i % 1 == 0:
            Count += 1
    Result.append(Count)
print('\n'.join(map(str, Result)))
