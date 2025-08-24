class Employee:
    company = "TechCorp"  
    def __init__(self,name,salary): 
        self.name = name
        self.salary = salary
    def print_details(self):
        info= f"Name: {self.name}, Salary:{self.salary}"    
        print(info)
    #staticmethod
    @staticmethod 
    def sum(a,b):
        return a + b  
    @classmethod
    def print_company(cls):
        print(cls.company)  

    @classmethod
    def  change_company(cls, new_company):
        cls.company = new_company
e1 = Employee("John", 50000)
e2 = Employee("Jane", 60000)        
print(Employee.company)
# print(Employee.name)  # This will raise an error
e1.print_details()
e2.print_details()
e1.print_company()  # Using class method
e1.change_company("jk putti")
e1.print_company()  
print(Employee.company)  # Using class method
print(e2.sum(10,20)) # Using static method