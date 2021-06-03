year = int(input())

if year<1918 :
    print("12.09.{}".format(year) if year % 4 ==0 else "13.09.{}".format(year))
elif year>1918:
    print("12.09.{}".format(year) if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "13.09.{}".format(year))   
else:
    print("26.09.1918")