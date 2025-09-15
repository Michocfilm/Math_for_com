num = int(input("Enter the multiplication table you want:"))
count = 12
while True:
    print(f"{num}*{count} = {num*count}")
    if(count == 1):
        break
    count -=1
