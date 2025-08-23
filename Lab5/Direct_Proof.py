def sum_by_actual(n):
    return(sum(range(1,n+1)))

def sum_by_formula(n):
    return(int((n*(n+1))/2))

def proving(a,b):
    return(a==b)

n = int(input("Input : "))
actual_sum = sum_by_actual(n)
formula_sum = sum_by_formula(n)
print("Actual sum =",actual_sum)
print("Sum from formula =",formula_sum)
print("Result :",proving(actual_sum,formula_sum))