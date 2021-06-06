height = list(map(int, input().split()))
Word = [height[ord(i)-97] for i in input()]
result = max(Word)*len(Word)
print(result)
