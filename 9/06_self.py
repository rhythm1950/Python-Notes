class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

rhythm = Employee()
rhythm.salary = 100000
rhythm.getSalary() # Employee.getSalary(rhythm)