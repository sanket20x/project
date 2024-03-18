n = int(input("Enter the fibo number"))
a=0
b=1
if n==1:
    print(a)
elif n>1:
    print(a)
    print(b)
    for i in range(2,n):
        
        c=a+b
        print(c)
        a=b
        b=c
else:
    print("Enter a positive integer")        
       
   
