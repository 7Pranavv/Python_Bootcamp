class Animal: 
    location ="Mars" # Class variable shared by all instances
    def __init__(self,name): # Constructor to initialize instance variable
        self.name = name
    def speak(self): # Method to be overridden in child class
        print("Animal speaks")
class Dog(Animal): # Dog class inherits from Animal class
    def speak(self):
        super().speak() # Calling the parent class method
        
        print("Bhau Bhau")
a = Animal("Dog")                    
a.speak()# Calling the method from the parent class
d = Dog("Lyka") # Creating an instance of Dog
d.speak() # Calling the overridden method
print(d.location) # Accessing class variable from the child class