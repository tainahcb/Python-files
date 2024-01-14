"""
W05 Prove: Project Milestone - Shopping Cart Program
Author: Tainah Correia Barreto
PC 103 - CSEPC 110
"""
# This shopping cart program allows the user to add items to a cart, view the items in the cart, remove items from the cart,
# compute the total price of the items in the cart, and quit the program.
# It also includes a creative feature: this program allows the user to specify the quantity of each item they would like to add to the cart,
# and provides a running total of the items in the cart, displaying the prices and quantities of the items to two decimal places and including the appropriate currency symbol.

# Initialize empty lists to store the names and prices of the items
item_names = []
item_prices = []
item_quantity = []

# Define the menu function
def menu():
    print()
    print("Welcome to the Shopping Cart Program!")
    print()
    print("Please choose an option:")
    print()
    print("1. Add a new item")
    print("2. Display the contents of the shopping cart")
    print("3. Remove an item")
    print("4. Compute the total")
    print("5. Quit")
print()
# Define the add_item function
def add_item():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item:"))
    item_names.append(name)
    item_prices.append(price)
    item_quantity.append(quantity)

# Define the display_cart function
def display_cart():
    print("Shopping Cart:")
    for i in range(len(item_names)):
        print(f"{i+1}. {item_names[i]} - ${item_prices[i]:.2f} - {item_quantity[i]}")

# Define the remove_item function
def remove_item():
    index = int(input("Enter the number of the item you want to remove: ")) - 1
    if index < len(item_names) and index >= 0:
        item_names.pop(index)
        item_prices.pop(index)
        item_quantity.pop(index)
        print("Item removed.")
    else:
        print("Invalid choice. Please try again.")

# Define the compute_total function
def compute_total():
    total = sum(price * quantity for price, quantity in zip(item_prices, item_quantity))
    print(f"The total amount of the prices of all the items in the shopping cart is: ${total:.2f}")
    
# Main program loop
while True:
    menu()
    print()
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        print()
        display_cart()
    elif choice == "3":
        print()
        remove_item()
    elif choice == "4":
        print()
        compute_total()
    elif choice == "5":
        print("Thank you for using the Shopping Cart Program!")
        break
    else:
        print("Invalid choice. Please try again.")
