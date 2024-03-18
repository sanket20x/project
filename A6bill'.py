def r(check,tip):
    tipp = check*(tip/100)
    total = check+tipp
    print(total)
check = int(input("Enter the check amount"))
tip = int(input("Enter the tip"))

r(check,tip)