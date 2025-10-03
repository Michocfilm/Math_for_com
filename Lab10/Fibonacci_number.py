import random
import time
import os

def difficulty(quantity:int):
    """ สำหรับสร้าง difficulty level  """
    arr = [0,1]
    count = 0
    try :
        for i in range(2,quantity):
            arr.append(arr[i-2]+arr[i-1])
        for i in range(3):
            start_index = random.randrange(0,quantity-5)
            lis = arr[start_index:start_index+5]
            print(f"Remember this sequence: {lis}")
            time.sleep(5)
            os.system('cls')
            kb = input("Enter the Fibonacci sequence: ").split()
            kb = [int(x) for x in kb]
            stop = False
            for j in range(len(lis)):
                if lis[j] != kb[j]:
                    stop = True
                    break
            if stop :
                print(f"Wrong! The correct sequence was {lis}\nYou guessed correctly in {count} out of 3 rounds")
                break
            print("Correct!")
            count +=  1
        if count == 3:
            print(f"You guessed correctly in {count} out of 3 rounds")
    except Exception as E:
        print(E)   


print("--- Fibonacci Memory Game ---")
choice = int(input("Choose difficulty level (1 = Easy, 2 = Medium, 3 = Hard):"))
match choice:
    case 1:
        difficulty(10)
    case 2:
        difficulty(20)
    case 3:
        difficulty(30)