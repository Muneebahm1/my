# Unused variable
x = 10

# Unused function argument
def multiply(a, b):
    return a * b

# Duplicate code
def add(a, b):
    result = a + b
    result += 10  # Duplicated addition
    return result

# Unreachable code
def foo():
    return 42
    print("This line is unreachable")

# Missing docstring
def subtract(a, b):
    return a - b

# Long method
def long_method():
    result = 0
    for i in range(1000):
        result += i
    return result

# Inefficient code
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Type hinting issue
def greet(name: str) -> str:
    return "Hello, " + name

# Division by zero
def divide(a, b):
    return a / b

result = divide(10, 0)
