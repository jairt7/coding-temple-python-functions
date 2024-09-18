# 2. The Shopping List Maker

print("Welcome to my shopping list creator.")
keep_going = True
shopping_list = []
while keep_going:
    print("Would you like to add an item, or remove an item, or are you done?")
    what_to_do = input("Valid inputs: 'add', 'remove', 'print', 'sort' 'done' ")
    if what_to_do == 'add':
        item = input("What would you like to put on the list? ")
        shopping_list.append(item)
        print("Item added. Let's keep going!")
    elif what_to_do == 'remove':
        item = input("What item would you like to remove? ")
        try:
            shopping_list.remove(item)
            print("Item removed. Let's keep going!")
        except ValueError:
            print("That wasn't on the list.")
    elif what_to_do == 'print':
        print("Got it. Here's your list:")
        for item in shopping_list:
            print(item)
    elif what_to_do == 'sort':
        shopping_list.sort()
        print("Sorted! Let's keep going.")
    elif what_to_do == 'done':
        keep_going = False
    else:
        print("Not a valid input.")
print()
print("Thanks for using my shopping list maker.")