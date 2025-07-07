class Point:
    def __init__(self, x, y):
        self.x = x
        self.y=y

    def sum(self,p):
        return Point((self.x + p.x),(self.y + p.y)) 
    def print_point(self):
        print(f"X is {self.x}and Y is {self.y}")
    def __add__(self,p):
        return Point((self.x + p.x),(self.y + p.y)) 



p1 = Point(10, 20)        
p2 = Point(30, 9) 
p=p1 + p2 # Using the overloaded + operator
p.print_point()        