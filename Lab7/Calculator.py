choice = input("Please select choice 1-5 only :")
num1 = float(input("Enter Number1 :"))
num2 = float(input("Enter Number2 :"))
print(type(num1))
match choice:
    case '1':
        result = num1 + num2
        choice = '+'
    case '2':
        result = num1 - num2
        choice = '-'
    case '3':
        result = num1 * num2
        choice = '*'
    case '4':
        result = num1 / num2
        choice = '/'
    case '5':
        result = num1 ** num2
        choice = '**'

print(f"{num1:.2f} {choice} {num2:.2f} = {result:.2f}")