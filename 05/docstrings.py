def add(A,V):
    """
    Adds two numbers A and V.

    Parameters:
    A (int or float): The first number.
    V (int or float): The second number.

    Returns:
    int or float: The sum of A and V.
    """
    c = A + V
    return c
  
print(add.__doc__)
print(add(3,4))