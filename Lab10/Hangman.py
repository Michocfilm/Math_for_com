import random
fruit = ("apple","banana","cherry","orange","strawberry")
choose = fruit[random.randrange(len(fruit))]
aeiou = ('a','e','i','o','u')

hint = [letter if letter in aeiou else '_' for letter in choose ]
print("Welcome to Hangman!")
while '_' in hint:
    print(f"Hint: {' '.join(hint)}")
    ans = input("Guess a letter:").lower()
    index = 0
    if ans in choose:
        collec = False
        for i in choose:
            if ans == i and hint[index] == '_':
                hint[index] = i
                collec = True
            else :
                index += 1
        if collec :
            print(f"Correct guess: {ans}")
        else :
            print(f"You already guessed '{ans}' correctly.")
    else :  
        print(f"Incorrect guess: {ans}")
print(f"Congratulations! You guessed the word '{choose}' correctly!")
