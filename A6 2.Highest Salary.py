n = int(input("Enter the number of employees"))
a1 = []
a2 = []
for i in range(n):
    ap1 = input("Enter the name of employee")
    a1.append(ap1)
print(a1)
for i in range(n):
    ap2 = input("Enter the salary")
    a2.append(ap2)
print(a2)

merge = dict(zip(a1,a2))
des = dict(sorted(merge.items(),key = lambda x:x[1], reverse= True))
print(des)

a3 = []
for i in des:
    a3.append(i)
print(a3)

a4=a3[0]
print(a4)




    
    



