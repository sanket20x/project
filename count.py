def employee():
    n = int(input("Enter the no"))
    if(n<=0):
        print("employee should be greater than 0")
        return
    
    employees={}
    for i in range(n):
        name = input("Enter the name of employee{i+1}")
        salary = int(input("Enter the salary"))
        employee[name]=salary
    if not employees:
        print("No employees provided")
        return
    
    maxi = max(employees.values())
    high = [name for name, salary in employees.items() if salary == maxi ]
    
    print(high)
    
    
