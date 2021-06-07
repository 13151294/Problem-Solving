for i in range(int(input())):
    Height = 0
    for j in range(int(input())+1):
        Height += (Height if ((j - 1) % 2 == 0 and j > 0) else 1)
    print(Height)
