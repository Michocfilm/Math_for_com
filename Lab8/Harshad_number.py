print("Harshad numbers between 1 and 100:")
count = 0
for i in range(1,101):
    n=i
    sum = 0
    while n > 0:
        sum += n % 10 
        n //= 10
    if(i%sum == 0):
        print(i,end="\t")
        count += 1
        if(count%10==0):
            print()