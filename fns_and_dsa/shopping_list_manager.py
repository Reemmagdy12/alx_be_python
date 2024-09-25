def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            added_item = input("Enter the item you want to add :")
            shopping_list.append(added_item)
            
        elif choice == '2':
            # Prompt for and remove an item
            removed_item = input ("Enter the name of the item to be removed:")
            if removed_item not in shopping_list :
                print("item does not exist")
            else:
                shopping_list.remove(removed_item)
            
        elif choice == '3':
            # Display the shopping list
            for i  in shopping_list:
                print(i)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()