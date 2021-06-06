n, jumpHeight = map(int, input().split())
MaxHurdles = max(list(map(int, input().split())))
if MaxHurdles > jumpHeight:
    print(MaxHurdles - jumpHeight)
else:
    print(0)
