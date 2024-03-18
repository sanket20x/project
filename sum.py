a = int(input("Enter the sum"))
adder = 0
for i in range(1,a+1):
    
    b=a%10
    adder=int(adder+b)
    a=a//10
print(adder)
