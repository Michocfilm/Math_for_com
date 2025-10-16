def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # ตัวอักษร
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'e':  # เข้ารหัส
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'd':  # ถอดรหัส
                result += chr((ord(char) - base - shift) % 26 + base)
        elif char.isdigit():
            # ตัวเลข 
            base = ord('0')
            if mode == 'e':  # เข้ารหัส => ตัวเลขลบ shift
                result += chr((ord(char) - base - shift) % 10 + base)
            elif mode == 'd':  # ถอดรหัส => ตัวเลขบวก shift
                result += chr((ord(char) - base + shift) % 10 + base)
        else:
            result += char
    return result


def reverse_each_word(text):
    words = text.split(' ')
    reversed_words = [''.join(reversed(word)) for word in words]
    return ' '.join(reversed_words)



while True:
    mode = input("กด e เข้ารหัส กด d ถอดรหัส กด q ออกจากโปรแกรม\n").lower()

    if mode == 'q':
        print("ออกจากโปรแกรม")
        break

    elif mode in ['e', 'd']:
        text = input("กรอกข้อความที่ต้องการ{}รหัส\n".format("เข้า" if mode == 'e' else "ถอด"))
        shift = int(input("กรอกจำนวนตัวอักษรที่ต้องการเลื่อน\n"))

        if mode == 'e':
            # เข้ารหัส
            encoded = caesar_cipher(text, shift, 'e')
            final_text = reverse_each_word(encoded)
            print("=" * 24)
            print(f"{text} ถูกเข้ารหัสเป็น: {final_text}")
            print("=" * 24)

        elif mode == 'd':
            # ถอดรหัส
            reversed_text = reverse_each_word(text)
            decoded = caesar_cipher(reversed_text, shift, 'd')
            print("=" * 24)
            print(f"{text} ถูกถอดรหัสเป็น: {decoded}")
            print("=" * 24)

    else:
        print("กรุณากรอกเฉพาะ e, d หรือ q เท่านั้น\n")

