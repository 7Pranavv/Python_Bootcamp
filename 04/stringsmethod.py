name="pranav rao"

#name[0]="R" # This will raise an error because strings are immutable in Python
a = len(name)  # Get the length of the string
print(a)
print (name.upper(),name)
print(name.lower())
print(name.title())  

text =" Hello, World! "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

hello="Pranav is best"
print(text.find("is"))
print(text.replace("best","awesome"))

fruits="apple,banana,orange"
print(fruits)  # Print the original string
print(fruits.split(","))  # Split the string into a list using comma as the delimiter
print (",".join(['Apple', 'Banana', 'Orange']))  # Join the list back into a string with commas
