n, step = map(int, input().split())
Cloud = [int(i) for i in input().split()][::step]
energy = 100
UseEnergy = len(Cloud)+(sum(Cloud)*2)
print(energy-UseEnergy)
