def check_positive_integer(n):
    try :
        num=int(n)
        assert 0<=num
        print(f"{num} is a positive integer")
    except:
        print(f"{n} is not a positive integer")

a = input("Input : ")
check_positive_integer(a)