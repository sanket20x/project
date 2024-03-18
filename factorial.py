a = int(input("Enter the number"))
c=0
while a>0:
    b=a%10
    c=int(c*10)*b
    a//10
print(c)
