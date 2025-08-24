class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Employee name is {self.name} and the salary is {self.salary}" 
       
    def __repr__(self):
        return f"Employee: {self.name} \nSalary:{self.salary}" 

    def __len__(self):
        return len(self.name)

e = Employee("John", 50000)
print(e.name,e.salary)
print(str(e))
print(repr(e))
print(len(e))  