for i in range(int(input())):
    Students, Threshold = map(int, input().split())
    StudentsList = [int(i) for i in input().split()]
    InThreshold = 0
    for i in StudentsList:
        InThreshold += (1 if i <= 0 else 0)
    print('NO' if InThreshold >= Threshold else 'YES')
