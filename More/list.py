import random
# name = list()
name = ["Michoc","ford","Max"]

name.append("Michoc")
name.append("MIFI")
name.insert(1,"Ford") # เอาไปแทรกเฉยๆ

name[1] = "Ohm" # เอาค่าไปแทน index นั้นๆ
name.insert(1,"max")

print(name)

count = len(name)
print(count)
for item in name:
    print(item)

random_name = random.randint(0,len(name)-1) # สุ่มตัวเลขเพื่มไปเป็น index 
print("random :",name[random_name])

name2 = ["too","bass"]
name.extend(name2) # การเอา list มารวมกัน
print(name)
print("---------------------------------")
new_list = []
for item in range(1,101):
    result = item*item 
    new_list.append(result)
print(new_list)

print("------------------------------------")

new_list2 = [item*item for item in range(1,101)] # ถ้าเป็น range จะเป็น 101-1
print(new_list2)

student = ["ford","max","to"]
update = []
# เขียนแบบเต็ม
# for person in student:
#     update.append(person.title())
# print(update)
# เขียนแบบย่อ
update=[person.title() for person in student ]
print(update)
print("-------------------------")
def two_dices():
    first = random.randint(1,6)
    second = random.randint(1,6)
    return first,second

dice_a,dice_b = two_dices()
print(dice_a,dice_b)