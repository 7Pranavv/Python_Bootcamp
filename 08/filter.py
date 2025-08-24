def is_greater_then_9(x):
    if x>9:
        return True
    else:
        return False
a = [1,3,5,4,234,450,32,98,32,515]    
new = list(filter(is_greater_then_9,a))
print(new)
# second way
well =list(filter(lambda x:x>9,a))
print(well)