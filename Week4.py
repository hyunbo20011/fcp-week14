def usqrt(y):
    if y < 0 or int(y) !=y:
        return -1
    
x = y
while x**2 >y:
    x=(x+y//x) // 2
return x

number int(input("Please enter a positive integer"))

square_root = isqrt(number)

if square_root == -1:
    print("Please enter a valid positive integer!")
else:
    print("Integer square root of", number, "is", square_root)