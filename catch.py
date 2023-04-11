def func1(x):
    if x < 0:
        raise ValueError("Negative numbers not allowed")
    return x**2

try:
    result = func1(-3)
except ValueError:
    print("An error was found")
else:
    print("the result is", result)