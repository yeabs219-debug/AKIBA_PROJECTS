name = input("Enter your name: ")
Basic_salary=float(input("Enter your basic salary: "))
Transport_allowance=  float(input("Enter your transport allowance: "))
Food_allowance= float(input("Enter your food allowance: "))

Gross_salary = Basic_salary+Transport_allowance+Food_allowance

print(f"""
========================================
             EMPLOYEE PAYSLIP
========================================

Employee: {name}

Basic Salary:          {Basic_salary} ETB
Transport Allowance:    {Transport_allowance} ETB
Food Allowance:         {Food_allowance} ETB
----------------------------------------
Gross Salary:          {Gross_salary} ETB
========================================

""")