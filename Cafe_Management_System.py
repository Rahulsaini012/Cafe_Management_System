print("Welcome to the Cafe Management System!")
print("---------------------------------------\n")

# Menu for the cafe
menu = {
    "Coffee": 2.5,
    "Tea": 1.8,
    "Sandwich": 5.0,
    "Cake": 3.0,
    "Smoothie": 4.0
}

# Initialize an empty order
order = {}

def display_menu():
    """Display the cafe menu."""
    print("Here's our menu:")
    for item, price in menu.items():
        print(f"{item:<15} ${price:.2f}")
    print("\n")

def add_item_to_order():
    """Add items to the customer's order."""
    item = input("Enter the item you'd like to order: ").strip()
    if item in menu:
        quantity = int(input(f"How many {item}s would you like to order? "))
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity
        print(f"{quantity} {item}(s) added to your order.\n")
    else:
        print(f"Sorry, {item} is not available on the menu.\n")

def view_bill():
    """View the current bill."""
    if not order:
        print("Your order is empty.\n")
        return
    print("Your current bill:")
    total = 0
    for item, quantity in order.items():
        cost = quantity * menu[item]
        total += cost
        print(f"{item:<15} x{quantity} = ${cost:.2f}")
    print(f"\nTotal: ${total:.2f}\n")

def cafe_management():
    """Main function to run the cafe management system."""
    while True:
        print("Options:")
        print("1. View Menu")
        print("2. Add Item to Order")
        print("3. View Bill")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        print("")
        
        if choice == "1":
            display_menu()
        elif choice == "2":
            add_item_to_order()
        elif choice == "3":
            view_bill()
        elif choice == "4":
            print("Thank you for visiting our cafe! Have a great day!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the cafe management system
cafe_management()