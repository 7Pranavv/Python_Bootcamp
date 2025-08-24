def decorator(func):
    def wrapper():
        print("I am about to execute a function")
        func()
        print("I have executed a function")
    return wrapper

@decorator #another way to apply the decorator
def say_hello():
    print("Hello, World!")
say_hello()  
'''
f looks like this:
def f():
print("I am about to execute a function")
print("Hello, World!")      
print("I have executed a function")
'''      
# f=decorator(say_hello)  # Calling the decorated function
# f()  # This will execute the wrapper function