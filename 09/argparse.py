import argparse

parser = argparse.ArgumentParser(description="Calci")

parser.add_argument("num1",type=float,help="First number")
parser.add_argument("num2",type=float,help="second number")
parser.add_argument("operation",choices=["add","sub","div","mul"])
help="Operation to perform"

args=parser.parse_args()
print(args)
if(args.operation == "add"):
    print(f"the result is {args.num1+args.num2}")
elif(args.operation == "sub"):
    print(f"the result is {args.num1-args.num2}")
elif(args.operation == "mul"):
    print(f"the result is {args.num1*args.num2}")
elif(args.operation == "div"):
    print(f"the result is {args.num1/args.num2}")

else:
    print("Some error occured")

  
    