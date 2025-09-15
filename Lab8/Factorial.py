num = int(input("Please enter a positive integer:"))
p = num
result = 1
while num > 0:
    result*=num
    num -= 1
print(f"The factorial of {p} is {result}")