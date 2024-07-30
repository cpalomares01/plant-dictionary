#My First CLI Application 7-28-2024
#I'd like to make an application that allows users to input given plants and details about them
#Ex. Golden Pothos, "Devil's Ivy", No Medicinal Purposes, Medium to Low light

def del_from_dictionary():
    try:
        print("Which entry would you like to delete? (Enter 'cancel' to cancel)")
        user = input("> ")
        if user == "cancel":
            print("Cancelled deleting")
            pass
        else:
            with open('plant_dictionary.txt', 'r') as file_input:
                with open('plant_dictionary.txt', 'w') as output:
                    for line in file_input:
                        if line != user:
                            output.write(line)
            print("Entry '" + user + "' removed.")
    except:
        print("An error has occurred.")

def print_dictionary():
    with open('plant_dictionary.txt', 'r') as file:
        for line in file:
            print(line.strip())

def add_to_dictionary():
    with open('plant_dictionary.txt', 'a') as file:
        print("What's the plant's name?")
        user = input("> ")
        file.write(user + ' , ')
        print("What's the plant's species?")
        user = input("> ")
        file.write(user + ' , ')
        print("What's the plant's medical use?")
        user = input("> ")
        file.write(user + ' , ')
        print("What's the plant's preferred light level?")
        user = input("> ")
        file.write(user + "\n")

def print_help_page():
    print("Here are the functions available to you:")
    print("help: shows this page of features and useful information")
    print("print: prints any available plants in the dictionary in a")
    print("clean and neat format")
    print("add: runs the add function which allows you to add a new")
    print("plant to your dictionary")
    print("del: runs the delete function which allows you to remove")
    print("a given entry from your dictionary")
    print("exit: exits the program")

#Main menu and their choices
def main_menu():
    print("Main Menu:")
    print("Enter 'help' for detailed instructions...")
    user = 0
    while user != "exit":
        user = input("> ")
        match user:
            case "help":
                print_help_page()
            case "print":
                print_dictionary()
            case "add":
                add_to_dictionary()
            case "del":
                del_from_dictionary()
            case "exit":
                pass
            case _:
                print("invalid input")

main_menu()