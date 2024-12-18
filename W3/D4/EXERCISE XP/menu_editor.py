from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("\nRestaurant Menu Management")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")
    choice = input("Enter your choice: ").upper()

    if choice == 'V':
        view_item()
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        remove_item_from_menu()
    elif choice == 'U':
        update_item_from_menu()
    elif choice == 'S':
        show_restaurant_menu()
    elif choice == 'E':
        print("Exiting... Here's the restaurant menu:")
        show_restaurant_menu()
        exit()
    else:
        print("Invalid choice. Please try again.")
    show_user_menu()

def view_item():
    name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item: {item[1]}, Price: {item[2]}")
    else:
        print("Item not found.")

def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = int(input("Enter the price of the item: "))
    item = MenuItem(name, price)
    try:
        item.save()
        print("Item was added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuItem(name, 0)
    try:
        item.delete()
        print("Item was deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def update_item_from_menu():
    current_name = input("Enter the current name of the item: ")
    new_name = input("Enter the new name of the item: ")
    new_price = int(input("Enter the new price of the item: "))
    item = MenuItem(current_name, 0)
    try:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("\nRestaurant Menu:")
        for item in items:
            print(f"- {item[1]}: {item[2]} NIS")
    else:
        print("Menu is empty.")

# Start the program
if __name__ == "__main__":
    show_user_menu()