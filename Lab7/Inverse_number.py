num = input("Please enter positive integer:")
try:
    n = int(num)
    assert 0<=n<=9999
    inverse = str(n)[::-1]
    print(f"Inverse number is {inverse}")
except :
    print(f"{num} is not a positive integer, exit !!!")