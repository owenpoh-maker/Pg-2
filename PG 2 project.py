# Stationery Inventory Management System
import csv
import os
from item_calculator import get_total


# Initial inventory data
inventory = {            
    "Pen": {"quantity": 200, "price": 1.20},
    "Pencil": {"quantity": 250, "price": 0.80},
    "Eraser": {"quantity": 150, "price": 0.50},
    "Glue Stick": {"quantity": 100, "price": 1.10},
    "Writing Book": {"quantity": 300, "price": 1.50}
}
# menu function to display options and handle user input
def menu():
    while True:
        clear_screen()
        print("===========================================")
        print("STATIONERY INVENTORY MANAGEMENT SYSTEM")
        print("===========================================")
        print("1 – To enter new stationery item")
        print("2 – To edit the stationery item")
        print("3 – To display the stationery item which was sold")
        print("4 – To display all the stationery items")
        print("5 – To save the list of all the stationery items in .CSV file")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            edit_item()
        elif choice == "3":
            sell_item()
        elif choice == "4":
            display_items()
        elif choice == "5":
            save_to_csv()
        else:
            print("Invalid option! Try again.")
            continue
        while True:
            cont = input("\nDo you want to continue? (y/n): ").lower()
            if cont == "y":
                break 
            elif cont == "n":
                print("Goodbye!")
                return 
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                
        
# Functions for each menu option
def add_item():
    name = input("Enter item name: ").strip()
    
    if not name: 
        print("Error: Item name cannot be blank!")
        return  # Exit the function early
    quantity = get_int("Enter quantity: ")
    price = get_float("Enter price: ")
    inventory[name] = {"quantity": quantity, "price": price}
    print(f"\n{name} added successfully!")

# Function to edit an existing item, with case-insensitive matching
def edit_item():
    name = input("Enter item name to edit: ").lower()
    match = None
    for key in inventory:
        if key.lower() == name:
            match = key
            break
        
    if match:
        quantity = get_int("Enter new quantity: ")
        price = get_float("Enter new price: ")
        inventory[match] = {"quantity": quantity, "price": price}
        print(f"{match} updated successfully!")
    else:
        print("Item not found!")

# Function to sell an item, with case-insensitive matching and stock check
def sell_item():
    name = input("Enter item name to sell: ").lower()
    match = None
    for key in inventory:
        if key.lower() == name:
            match = key
            break

    if match:
        available_quantity = inventory[match]["quantity"]
        print(f"Available quantity of {match}: {available_quantity}")
        quantity_to_sell = get_int("Enter quantity to sell: ")
        
        if quantity_to_sell > available_quantity:
            print("Not enough stock! Try again.")
        else:
            inventory[match]["quantity"] -= quantity_to_sell
            total_price = quantity_to_sell * inventory[match]["price"]
            print(f"Sold {quantity_to_sell} of {match} for ${total_price:.2f}")
    else:
        print("Item not found!")

# Function to display all items in the inventory
def display_items():
    print("\nInventory:")
    print("{:<15} {:<10} {:<10} {:<10}".format("Name", "Quantity", "Price", "Total"))
    print("-" * 50)

    for item, details in inventory.items():
        total = calculate_total_price(item)
        print("{:<15} {:<10} {:<10.2f} {:<10.2f}".format(
              item, details["quantity"], details["price"], total))
    print("-" * 50)
    # ← move these INSIDE display_items, outside the for loop
    total_items = len(inventory)
    total_value = sum(calculate_total_price(item) for item in inventory)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def calculate_total_price(item):
    return get_total(inventory[item]["quantity"], inventory[item]["price"])

# Function to save inventory data to a CSV file
def save_to_csv():
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Quantity", "Price", "Total"])
        for item, details in inventory.items():
            writer.writerow([item, details["quantity"], details["price"], calculate_total_price(item)])
    print("Inventory saved to inventory.csv")

# Function to get a valid integer input for quantity
def get_int(quantity):
    while True:
        try:
            value = int(input(quantity))
            if value < 0:
                print("Must be a positive number. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a whole number.")
# Function to get a valid float input for price
def get_float(price):
    while True:
        try:
            value = float(input(price))
            if value < 0:
                print("Must be a positive number. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

menu()
