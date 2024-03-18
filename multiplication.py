while True:
    a = input("Enter the  number ")
   
    if a.isdigit():
        break
    else:
        print("invalid input")
a = int(a)

for i in range(1,11+1):
    print(a*i)


        
    