def cal_GCD(a,b):
    try:
        return cal_GCD(b, a % b)
    except ZeroDivisionError:
        return a

try:
    num1 = float(input("Positive Integer1 :"))
    assert 0<=num1
    num2 = float(input("Positive Integer2 :"))
    assert 0<=num2
    print(f"GCD : {cal_GCD(num1,num2)}")
except:
    print("as is not positive integer, exit !!!")