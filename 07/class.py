class Employee:
    company = "Google"  # Class variable

    def get_salary(self):
        print(self) # 'self' refers to the instance of the class
        return 100000
    
e=Employee() # Creating an instance of Employee
print(e.get_salary())  # Accessing instance method  

e2=Employee()  # Creating another instance of Employee  
print(e2.get_salary())
print(e.company)
print(e2.company)