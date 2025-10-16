all = "abcdefghijklmnopqrstuvwxyz"
def encode(text,shift):
    encoded = ""
    for char in text:
        if char.isalpha():
            char_isupper = char.isupper()
            char_lower = char.lower()
            index = all.find(char_lower)
            if index != -1:
                new_index = (index+shift)%len(all)
                if char_isupper:
                    encoded += all[new_index].upper()
                else :
                    encoded += all[new_index]
            else :
                encoded += char
        else :
            encoded += char
    return encoded

def decode(text,shift):
    decoded = ""
    for char in text :
        if char.isalpha():
            upper_char = char.isupper()
            char_lower = char.lower()
            index = all.find(char_lower)
            if index != -1:
                new_index = (index-shift)%len(all)
                if upper_char:
                    decoded += all[new_index].upper()
                else :
                    decoded += all[new_index]
            else :
                decoded += char
        else :
            decoded += char
    return decoded

while True:
    choice = input("Encode 1 , Decode 2 : ")
    match choice:
        case "1":
            text = input("Enter your word : ")
            shift = int(input("Enter shift : "))
            print(encode(text,shift))
        case "2":
            text = input("Enter your word : ")
            shift = int(input("Enter shift : "))
            print(decode(text,shift))
        case _:
            break