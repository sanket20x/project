a = input("Enter the string")
if a.isupper():
    swap=a.lower()
    print( "swapcase ",swap)
elif a.islower():
    swap=a.upper()
    print( "swapcase ",swap)
else:
    swap=a.swapcase()
    print(swap)