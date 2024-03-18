while True:
    n=input("Enter the number for fibo series")
    if n.isdigit():
        break
    else:
        print("Invalid input")
    
n = int(n)
a=0
b=1
if n==1:
    print(a)
elif n>1:
    print(a)
    print(a)
    
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c
        
