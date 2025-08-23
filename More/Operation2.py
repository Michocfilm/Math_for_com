text = input("Input : ")
# แปลงตัวอักษรตามตำแหน่ง 1, 3, 6 (index 0, 2, 5)
result = (
    text[0].upper() +   # p
    text[1] +           # y
    text[2].upper() +   # t
    text[3] +           # h
    text[4] +           # o
    text[5].upper()     # n
)
print("Output :", result)

