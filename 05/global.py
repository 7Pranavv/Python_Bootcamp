def sum(a,b):
    print("This is a global variable")
    c = a + b
    global z  # Declare z as a global variable
    z = 0  # This will modify the global z variable
    return c
z = 2 
print(sum(3,4))
print(z)  