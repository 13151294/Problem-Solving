def roundFunc(x):
    result = round(x/5)*5
    if result >= 40:
        if x <= result:
            return result
        else:
            return x
    else:
        return x
for i in range(int(input())):
    print(roundFunc(int(input())))