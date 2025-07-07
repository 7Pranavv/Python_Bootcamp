def sum(a,b):
    c = a+b
    z=4 # This is a local variable, it will not affect the global z
    return c
def sub(a,b):
    z=5
    print("hello")

z = 8 # This is a global variable, it can be accessed anywhere in the module
print(z)
print(sum(3,4))    
print(z)