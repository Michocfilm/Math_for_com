hour = int(input("Hour : "))
rate = 123.50
salary = (float(hour)*rate).__ceil__() # .__ceil__()สำหรับปัดเศษขึ้น
loss = (salary)-(hour*rate)
print(f"Salary : {salary} Baht \nLoss : {loss}")