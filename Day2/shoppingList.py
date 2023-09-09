# shopping list
# menu driven code to
# 1. add item (after check else alert)
# remove item
# print

shopping_list = []

def print_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. Print list")
    print("4. Quit")

while True:
    print_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        item = input("Enter item name: ").lower()
        if item in shopping_list:
            print(item, "is already in the shopping list.")
        else:
            shopping_list.append(item)
            print(item, "has been added to the shopping list.")
            
    elif choice == "2":
        item = input("Enter item name: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed from the shopping list.")
        else:
            print(item, "is not in the shopping list.")
            
    elif choice == "3":
        print("Shopping List:")
        for item in shopping_list:
            print(item)
            
    elif choice == "4":
        break

