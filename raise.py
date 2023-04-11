def func1(x):
    result = func2(x)

def func2(x):
    result = func3(x)

def func3(x):
    result = func4(x)

def func4(x):
    if x <0:
        raise ValueError("Negative numbers are not allowed!")
    
value = func1(-10)
