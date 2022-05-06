class Employee:
    company = "Google"
    salary = 100

rhythm = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# rhythm.salary = 300
# rajni.salary = 400
rhythm.salary = 45
print(rhythm.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 