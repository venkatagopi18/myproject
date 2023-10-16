def employee_details():
    d = {}  
    no_employes = int(input("Enter the number of employees: "))
    for i in range(no_employes):
        emp_name = input("Enter employee name: ")
        emp_domain = input("Enter domain: ")
        emp_id = input("Enter employee id: ")
        emp_email = input("Enter email id: ")
        
        d[emp_id] = {"name":emp_name,"id":emp_id, "email":emp_email,"domain":emp_domain}
    print(d)
    particular_emp_details=input("enter_emp_details: ")
    for i in d:
        values=list(d[i].values())
        # print(values)
        if particular_emp_details in values:
            print(d[i])
employee_details()

