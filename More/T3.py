# kb = input("en: ")
# print(kb+"\r"+"\\")
import random
result = random.randint(0,9)
match result:
    case 9 :
        print("miss you")
    case 5 :
        print("what di")
    case _:
        print("you")