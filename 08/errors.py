# while True:
#     try:
#      a = int(input("Enter number 1"))
#      b = int(input("Enter number 2"))

#      print(f"The sum is{a+b}")
#     except ValueError:
#       print("Please dont perform bad tasks")
#     except ZeroDivisionError:
#       print("dont divide by 0")   
     
#     except Exception as e:
#      print("YE kya hogya",e) 

a = int(input("Enter number 1"))
b = int(input("Enter number 2"))

if b == 0:
    raise ValueError("Dont Divide by zero")
print(f"The sum is{a/b}")