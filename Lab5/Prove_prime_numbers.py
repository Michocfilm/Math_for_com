def is_prime(n):
    return(n==2 or (n>1 and pow(2,n-1,n)==1 and n not in(561,1105,1729)))

n = int(input("Input : "))
print("Prime :",is_prime(n))