import datetime

# ====== EMPTY DICTIONARY  ====== 
inventory = {}

# ====== REPEATING FUNCTIONS ====== 
# -> Functions for Errors <-

def batchdate(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%y/%m/%d")
    except ValueError:
        print("Invalid date format. Use YY/MM/DD.\n")
        return None

def errormessage(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.\n")

#  ====== ADDING THE PRODUCT INTO THE INVENTORY  ====== 

def add_product():
    name = input("Enter product name: ").strip().lower()
    date_str = input("Enter batch date (YY/MM/DD): ").strip()
    date = batchdate(date_str)
    if not date:
        return

    qty = errormessage("Enter quantity: ")

    # USES THE LAST LOGGED UNIT COST. 
    if name in inventory and len(inventory[name]) > 0:
        same_cost = input("Same cost as last logged batch? (yes/no): ").strip().lower()
        if same_cost == "yes":
            unitcost = inventory[name][-1]["cost"]
        else:
            unitcost = errormessage("Enter new unit cost: ")
    else:
        unitcost = errormessage("Enter cost per unit: ")

    batch = {
        "date": date_str, 
        "qty": qty,
        "cost": unitcost
    }
    # IF PRODUCT DOESN'T EXIST YET
    if name not in inventory:
        inventory[name] = []
    inventory[name].append(batch)

    print(f"✅Product successfully added to inventory. New tech product batch added!\n{qty} unit(s) of {name.title()} (Date: {date_str}).\n")

#  ====== REMOVING A PRODUCT FROM THE INVENTORY  ====== 

def remove_product():
    name = input("Product to remove: ").strip().lower()
    if name not in inventory or len(inventory[name]) == 0:
        print("Product not found.\n")
        return

    qtyremove = errormessage("How many units to remove?: ")

    inventory[name].sort(key=lambda b: batchdate(b["date"]), reverse=True)

    removed = 0
    while qtyremove > 0 and inventory[name]:
        batch = inventory[name][0]
        if batch["qty"] <= qtyremove:
            qtyremove -= batch["qty"]
            removed += batch["qty"]
            inventory[name].pop(0)
        else:
            batch["qty"] -= qtyremove
            removed += qtyremove
            qtyremove = 0

    if removed > 0:
        print(f"🗑️Product successfully removed from the inventory. Removed {removed} unit(s) of {name.title()} from your tech inventory.\n")
    else:
        print("⚠️ Not enough stock to remove the requested quantity!\n")

#  ====== DISPLAYING THE WHOLE INVENTORY ====== 

def check_inventory():
    if len(inventory) == 0:
        print("📭 Inventory is currently empty.\n")
        return

    print("\n🖥️ Current Technology Inventory Overview:")
    print("{:<15} {:<19} {:<10} {:<10}".format("Product", "Batch Date", "Qty", "Unit Cost"))
    print("-" * 60)
    for name in sorted(inventory):
        for batch in sorted(inventory[name], key=lambda b: batchdate(b["date"]), reverse=True):
            print("{:<15} {:<19} {:<10} {:<10}".format(name.title(), batch["date"], batch["qty"], batch["cost"]))
    print()

#  ====== SEARCHING FOR A PRODUCT ====== 

def search_product():
    name = input("Enter product name to search: ").strip().lower()

    if name in inventory and inventory[name]:
        sorted_batches = sorted(inventory[name], key=lambda b: batchdate(b["date"]), reverse=True)

        print(f"\n🔍 Search Results for {name.title()} in Tech Inventory:")
        print("{:<20} {:<8} {:<10}".format("Batch Date", "Qty", "Unit Cost"))
        print("-" * 40)
        for batch in sorted_batches:
            print("{:<20} {:<8} {:<10}".format(batch["date"], batch["qty"], batch["cost"]))
        print()
    else:
        print("Product not found.\n")

#  ====== THE MAIN MENU ====== 

def menu():
    while True:
        print("========= TECH INVENTORY MENU =========")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Inventory")
        print("4. Search for a Product")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            check_inventory()
        elif choice == "4":
            search_product()
        elif choice == "5":
            print("👋 Exiting Tech Inventory System. See you next time!")
            break
        else:
            print("Invalid choice! Try again.\n")

#  ====== THE START OF OUR PROGRAM ====== 

print("📦 Welcome to LifoStack — Your Technology Retail-Friendly Inventory System!\n")

while True:
    start = input("Would you like to manage your tech retail inventory now? (yes/no): ").strip().lower()
    if start == "yes":
        menu()
        break
    elif start == "no":
        print("Okay, goodbye!")
        break
    else:
        print("Please enter 'yes' or 'no'.\n")
