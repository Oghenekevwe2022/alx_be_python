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
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                # Prompt for adding an item
                item = input("Enter the item to add: ")
                item_name = item.lower()
                if item_name in shopping_list:
                    print(f"{item.capitalize()} already exists.")
                    add = input("would you like to keep it? (Y/N)").lower()
                    if add == "y":
                        print(f"{item.capitalize()} is already on the list.")
                    else:
                        print(f"{item.capitalize()} was not added.")
                else:
                    shopping_list.append(item_name)
                            
            elif choice == 2:
                # Prompt to remove an item
                item = input("Enter item to be deleted: ")
                item_name = item.lower()
                if item_name in shopping_list:
                    shopping_list.remove(item_name)
                    print(f"{item.capitalize()} has been removed from the list")
                else:
                    print(f"{item.capitalize()} does not exist in the list.")
                
            elif choice == 3:
                # View the shopping list
                if not shopping_list:
                    print("The shopping list is empty")
                else:
                    print("\nShopping list")
                    for index, item in enumerate(shopping_list, start=1):
                        print(f"{index}. {item.capitalize()}")
                        # print("Goodbye")
                        # break
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
                print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    main()