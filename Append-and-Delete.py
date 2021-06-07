FirstTxt = input()
SecondTxt = input()
Budget = int(input())
MinLength = len(FirstTxt)
Len1 = len(FirstTxt)
Len2 = len(SecondTxt)
while FirstTxt[:MinLength] != SecondTxt[:MinLength]:
    MinLength -= 1
Cost = len(FirstTxt[MinLength:] + SecondTxt[MinLength:])
if Cost > Budget:
    print("No")
elif Len1 + Len2 <= Budget:
    print("Yes")
elif 2*len(max(FirstTxt, SecondTxt))< Budget:
    print("Yes")
elif Budget%2 == Cost%2:
    print("Yes")
else:
    print("No")
