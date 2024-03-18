a = input("Enter the string")
if a.isupper():
    swap=a.islower()
   
elif a.islower():
    swap=a.isupper()
    
else:
    swap=a.swapcase()
print("swapcase is",swap)

    
    
    