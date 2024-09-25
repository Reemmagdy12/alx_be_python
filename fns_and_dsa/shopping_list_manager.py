def display_menu():
    print("Shopping List Manager")  # Print the title
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()  # Updated prompt text
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()  # Updated prompt text
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()