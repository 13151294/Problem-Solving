n = int(input())
command = list(input())
def countValley(command):
    y = 0
    valley = 0
    for script in command:
        if script == "U":
            y += 1
        elif script == "D":
            y -= 1
        
        if (script == "U") and (y == 0):
            valley += 1
    return valley
print(countValley(command))