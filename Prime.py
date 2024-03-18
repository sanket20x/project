while True:
    a =input("Enter the 1st no")
    b= input("Enter the 2nd no")
    a
    if a.isdigit() and b.isdigit():
        break
    else:
        print("Invalid input")
a =int(a)
b =int(b)

for i in range (a,b+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)
        
 
    
        