a = int(input("Enter number 1"))
b = int(input("Enter number 2"))
try:
    c=a/b
except Exception as e:
    print(e) 
finally:
    print("this is always executed")       