# name = input("Name: ")
# surename = input("Surename: ")
# age = input("Age: ")
# weight = input("Weight: ")
# height = input("Height: ")

# print("Name:",name,surename)
# print("Age:",age,"year old")
# print("Weight/Height:",weight+"/"+height)

name = {"t":"tello","w":"what","s":"say"}
popkey = name.pop("t",None)
del name["s"]
print(popkey)
print(name)