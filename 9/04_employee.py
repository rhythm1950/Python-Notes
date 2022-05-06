class Employee:
    company = "Google"
    salary = 100

rhythm = Employee()
rajni = Employee()
rhythm.salary = 300
rajni.salary = 400

print(rhythm.company)
print(rajni.company)
Employee.company = "YouTube"
print(rhythm.company)
print(rajni.company)
print(rhythm.salary)
print(rajni.salary)