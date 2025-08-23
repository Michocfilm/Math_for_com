hour = int(input("Hour : "))
rate = 123.50
salary = (hour*rate.__ceil__())
loss = (salary)-(hour*rate)
print(f"Salary : {salary} Baht \nLoss : {loss}")