def main():
    shopping_list = []

    while True:
        print("\n--- Shopping List Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            if not shopping_list:
                print("The shopping list is already empty.")
                continue

            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == '4':
            print("Exiting the shopping list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
