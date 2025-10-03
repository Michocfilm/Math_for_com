def display_inventory(inventory:dict):
    print("Inventory list:")
    if not inventory:
        print("No products in inventory.")
    else:
        for key,value in inventory.items():
            print(f"{key} : {value}")
        

def update_inventory(inventory:dict):
    key = input("Enter the product name you want to update:").title()
    if key in inventory:
        value = int(input("Enter the quantity to add or subtract:"))
        test = inventory[key] + value
        if test < 0 :
            print(f"Cannot reduce the quantity of {key} because it will result in a negative amount!")
        else:
            inventory[key] = test
            print(f"The updated quantity of Laptop is:{test}")
            return inventory[key]
    else:
        confirm = input(f"{key} is not in the inventory. Would you like to add it? (y/n):")
        if confirm.lower() == "y" :
            value = int(input("Enter the quantity to add or subtract:"))
            return inventory.setdefault(key,value)
    
def delete_inventory(inventory:dict):
    key = input("Enter the product name you want to delete:").title()
    confirm = input("Are you sure you want to delete Tablet? (y/n):").lower()
    if key in inventory :
        if confirm.lower() == "y" :
            del inventory[key]
            print(f"{key} has been deleted from the inventory.")
            return inventory
    else:
        print(f"Don't have {key} in inventory")

products = {
    "Laptop":10,
    "Phone":25,
    "Tablet":15
}
while True :
    print("Inventory Management System:\n1. View inventory list\n2. Add/Reduce products\n3. Delete products\n4. Exit the program")
    cin = input("Select an option: ")
    match cin:
        case "1":
            display_inventory(products)
        case "2":
            update_inventory(products)
        case "3":
            delete_inventory(products)
        case "4":
            break
