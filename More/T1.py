# First_name = input("Your Name : ")
# print("Your name is : "+First_name)
# Age = input("Your Age : ")
# print("Your Age is : "+Age)
# print("ABC\bZ") #จะลบข้อความก่อนหน้าและเอาข้อความข้างหลังไปแทนที่
# print("ABC\rZ") #จะลบข้อควาด้านหน้าและเอาข้อความข้างหลังไปแทนที่
# print("ABCZ","FIlm") #ถ้าเชื่อมด้วยเครื่องมหาย + จะไม่มีเว้นวรรค ถ้าเชื่อมด้วย , จะมีเว้นวรรค1ช่อง
# print("Hello",end=" ") #คือจะแค่เว้นวรรคแล้วนำข้อมูลจากคำสั่งบรรทัดต่อไปมาต่อท้าย
# print("world")
import math
print("test","jo",end="")
print(len("HEL".lower()))
num = 12
num1 = num
num2 = 12
result = int(num)
resultt = math.floor(num)
print(result,resultt)
print(type(num))
print(id(num1),id(num2))
print(hex(id(num)))
if 10 == 10:
    pass
else :
    print("DD")

print(round(3.535,2)) # round จะปัดเศษขึ้นเมื่อเกิน0.5และปัดลงเมื่อน้อยกว่า0.5 แต่ถ้าเศษ ช 0.5 แล้วจำนวนเต็มเป็นเลขคู่จะไม่ปัดขึ้น แต่ถ้าจนต.เป็นเลขคี่จะปัดขึ้นทันที