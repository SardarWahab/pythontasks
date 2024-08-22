# 1. Inventory Management System
# Description: Create a program to manage an inventory of products. The program should allow you to:

# Add new products (with details like name, price, and quantity).
# Update the quantity of existing products.
# Display all products in the inventory.
# Search for a product by name and display its details.
# Concepts Used: Dictionary, List, Input/Output, Functions.


# Step 1: Define the inventory dictionary
print("Inventery management system")
inventory = {}

# Step 2: Function to add a new product
def add_product(name, price, quantity):
    inventory[name] = {'price': price, 'quantity': quantity}
    print(f"Product {name} added to inventory.")

# Step 3: Function to update the quantity of an existing product
def update_quantity(name, quantity):
    if name in inventory:
        inventory[name]['quantity'] = quantity
        print(f"Quantity of {name} updated to {quantity}.")
    else:
        print(f"Product {name} not found in inventory.")

# Step 4: Function to display all products in the inventory
def display_inventory():
    if inventory:
        print("\nInventory:")
        for name, details in inventory.items():
            print(f"Product: {name}, Price: ${details['price']}, Quantity: {details['quantity']}")
    else:
        print("Inventory is empty.")

# Step 5: Function to search for a product by name
def search_product(name):
    if name in inventory:
        details = inventory[name]
        print(f"Product: {name}, Price: ${details['price']}, Quantity: {details['quantity']}")
    else:
        print(f"Product {name} not found in inventory.")

# Step 6: Main loop to interact with the system
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add New Product")
        print("2. Update Product Quantity")
        print("3. Display All Products")
        print("4. Search for a Product")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(name, price, quantity)
        
        elif choice == '2':
            name = input("Enter product name to update quantity: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(name, quantity)
        
        elif choice == '3':
            display_inventory()
        
        elif choice == '4':
            name = input("Enter product name to search: ")
            search_product(name)
        
        elif choice == '5':
            print("Exiting the Inventory Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main loop
# main()

