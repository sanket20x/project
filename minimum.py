while True:
    a = input("Enter the 1st number: ")
    b = input("Enter the 2nd number: ")
    c = input("Enter the 3rd number: ")
    d = input("Enter the 4th number: ")
    
    if a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit():
        break
    else:
        print("Invalid input")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

minim = min(a, b, c, d)
print("The minimum number is:", minim)