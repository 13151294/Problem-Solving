Zone1, Zone2 = (int(i) for i in input().split())
AppleTreePos, OrangeTreePos = (int(i) for i in input().split())
Apples, Oranges = [int(i) for i in input().split()]
AppleDistance = [int(i) for i in input().split()]
OrangeDistance = [int(i) for i in input().split()]
AppleInZone = 0 
OrangeInZone = 0
for i in range(len(AppleDistance)):
    ApplePos = AppleTreePos + AppleDistance[i]
    if (Zone1 <= ApplePos <= Zone2):
        AppleInZone += 1
print(AppleInZone)
for i in range(len(OrangeDistance)):
    OrangePos = OrangeTreePos + OrangeDistance[i]
    if (Zone1 <= OrangePos <= Zone2):
        OrangeInZone += 1
print(OrangeInZone)