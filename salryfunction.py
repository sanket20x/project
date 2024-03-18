def higest_salary():
    employee={}
    
    while True:
        
        name=input("Enter the name")
        if name=="done":
            break
        salary=input("enter the salary ")

        employee[name]=salary
 
    max_salary=max(employee.values())             
    high =[name for name, salary in employee.items()  if salary==max_salary]
    print(max_salary)
    print(high)    
higest_salary()
