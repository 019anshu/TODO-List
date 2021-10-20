
# * TO DO APPLICATION

# we need to import prettytable module for creating beautiful ascii table for our App.
from prettytable import PrettyTable

print("\nMy TO-DO List.")

instructions = "\n1: Enter A or a to add new TO-DO.\n2: Enter D or d to delete TO-DO.\n3: Enter U or u to update TO-DO.\n4: Enter E or e to exit the program.\n5: Enter L or l to check your TO-DO List."
print(instructions)

# List to add all the information in our todo list
my_todo_list = []

x = PrettyTable()
# we need to make a seperate function


def my_list():
    if my_todo_list:
        x.field_names = ["Item Names"]
        for i in my_todo_list:
            # add new row to our prettytble on every iteration.
            x.add_row([i])
        # get title for each to-do.
        # x.field_names = ["Added on Date"]

        print(x.get_string(title="TO DO List"))
        # clear previous info, every timee the table is reloaded
        # update our list with new information
        x.clear_rows()
    else:
        print("Your TO-DO List is Empty.\n Add some now!")


running = True
while running:
    # get user input
    user_input = (
        input("\nWhat do you want to do? (A, D, U, E, L): ").lower()).strip()
    # my_list()

    # Add new items to the todo list
    if user_input == "a":
        new_todo = (input("\n Please enter your new TODO: ").lower()).strip()
        if new_todo.isspace() or new_todo == "":
            print("\n Please enter something.")
        else:
            print(f"\n Your current TODO is \'{new_todo}\'.")
            # append the new todo to the TODO list
            my_todo_list.append(new_todo)

    # delete items from the todo list
    elif user_input == "d":
        while True:
            my_list()
            # ask the user to enter the todo to be deleted
            item_name = (
                input("\nPlease enter a name of an item you want to delete: ").lower()).strip()
            # using try catch to avoid any exception.
            try:
                # checking if the item is present in the Todo List
                if item_name in my_todo_list:
                    choice = (input(
                        f"\n Are you sure to delete \'{item_name}\' from your TODO List? (y/n) : ")).strip()
                    if choice == 'y':
                        my_todo_list.remove(item_name)
                        print("\nYour updated TO-DO List:")
                        my_list()
                        break
                else:
                    print("Item not found.")
            except Exception:
                print("Something went wrong.")

    # update the todo list
    elif user_input == "u":
        while True:
            my_list()
            # ask the user to enter the todo to be deleted
            item_name = (
                input("\n Please enter a name of an item you want to update: ").lower()).strip()
            # using try catch to avoid any exception.
            try:
                # checking if the item is present in the Todo List
                if item_name in my_todo_list:
                    choice = (input(
                        f"\n Are you sure to update \'{item_name}\' from your TODO List? (y/n) : ")).strip()
                    if choice == 'y':
                        updated_item = (input(
                            f" Please enter a name you want to update \'{item_name}\' with: ").lower()).strip()
                        index = my_todo_list.index(item_name)
                        my_todo_list[index] = updated_item
                        print("\nYour updated TO-DO List:")
                        my_list()
                        break
                else:
                    print("Item not found.")
            except Exception:
                print("Something went wrong.")

    # exit the program
    elif user_input == "e":
        ask_user = (input("\nAre you sure to exit? (y/n): ").lower()).strip()
        if ask_user =="y":
            running = False

    # print the todo list
    elif user_input == "l":
        my_list()

    # check if nothing is made input
    elif user_input.isspace():
        print("Please enter something.")

    # in case of invalid input
    else:
        print("Please enter a valid value.")
