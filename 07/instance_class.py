class Employee:
    company ="Google"
    def __init__(self,salary, name,bond,company):
        self.salary= salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is{self.name}and salary is {self.salary} and bond is {self.bond}")
e1 = Employee(134000, "Pranav", 2, "Microsoft") 
print(e1.company) # Accessing instance variable
print(Employee.company)  # Accessing class variable

#Object introspection
print(dir(e1))  # List all attributes and methods of the object