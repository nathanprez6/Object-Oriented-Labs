# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 22, 2025
# Description:  A program that allows the user to view, search, and modify a contact list
# made up of contact objects.

import check_input
from contact import Contact

def read_file():
    """ 
    Open a file and reads in each contact (one per line), then construct a Contact
    object using the data, and stores the Contact object in the list of contacts.

    Args:
        None

    Returns: 
        The list of contacts 
    """
    contacts = []
    with open("addresses.txt", "r") as file:
        for line in file:
            fn, ln, ph, addr, city, zip = line.strip().split(",")
            contacts.append(Contact(fn, ln, ph, addr, city, zip))
    contacts.sort()
    return contacts

def write_file(contacts):
    """ 
    Open a file for writing, loops through the contacts list and writes each contact
    to the file using the repr method.

    Args:
        contacts (list): a list of contacts

    Returns: 
        None 
    """
    with open("addresses.txt", "w") as file:
        for c in contacts:
            file.write(repr(c) + "\n")
    

def get_menu_choice():
    """ 
    Displays the main menu to the user and then prompts the user for a valid input.

    Args:
        None

    Returns: 
        An integer value of the user's choice 
    """
    print("Rolodex Menu:\n1. Display Contacts\n2. Add Contact\n" \
    "3. Search Contacts\n4. Modify Contact\n5. Save and Quit")

    menu_choice = check_input.get_int_range("Enter your choice (1-5): ", 1, 5)
    return menu_choice

def modify_contact(cont):
    """ 
    Displays the modify menu to the user, gets the user’s valid input, then, based on the user’s choice, 
    prompts the user for the information they’d like to change, and then updates the appropriate attribute
    for the contact.

    Args:
        cont (Contact object): the Contact object to be modified

    Returns: 
        None 
    """
    mod_menu = "\nModify Menu:\n1. First Name\n2. Last Name\n3. Phone \n4. Address\n5. City\n6. Zip \n7. Save"
    repeat = True

    while repeat:
        print(mod_menu)
        choice = check_input.get_int_range(">", 1, 7)
        if choice == 1: 
            cont.fn = input("Enter first name: ")
        elif choice == 2: 
            cont.ln = input("Enter last name: ")
        elif choice == 3: 
            cont.ph = input("Enter phone #: ")
        elif choice == 4: 
            cont.addr = input("Enter address: ")
        elif choice == 5:
            cont.city = input("Enter city: ")
        elif choice == 6:
            cont.zip = input("Enter zip: ")
        elif choice == 7:
            repeat = False
        

def main():
    contacts = read_file()
    repeat = True

    # Loops until user chooses to Save and Quit
    while repeat:
        choice = get_menu_choice()
        if choice == 1:
        # Displays Contact
            print("Number of contacts: " + str(len(contacts)))
            for i, contact in enumerate(contacts, start = 1):
                print(f"{i}. {contact}\n")
        elif choice == 2:
        # Add New Contact
            print("Enter new contact:")
            fn = input("First name: ")
            ln = input("Last name: ")
            ph = input("Phone #: ")
            addr = input("Address: ")
            city = input("City: ")
            zip = input("Zip: ")
            print()

            contacts.append(Contact(fn, ln, ph, addr, city, zip))
            contacts.sort()
            write_file(contacts)
        elif choice == 3:
        # Search Contact
            search_choice = check_input.get_int_range("Search:\n1. Search by last name\n2. Search by Zip\n>", 1, 2)
            if search_choice == 1:
            # Search by Last Name
                ln_choice = input("Enter last name: ")
                found = False
                for c in contacts:
                    if c.ln == ln_choice:
                        found = True
                        print(c)
                        print()
                if not found:
                    print("Contact not found.")
            if search_choice == 2:
            # Search by Zip
                zip_choice = input("Enter Zip: ")
                found = False
                for c in contacts:
                    if c.zip == zip_choice:
                        found = True
                        print(c)
                        print()
                if not found:
                    print("Contact not found.")
        elif choice == 4:
        # Modify Contact
            fn_choice = input("Enter first name: ")
            ln_choice = input("Enter last name: ")
            found = False
            for c in contacts:
                if c.fn == fn_choice and c.ln == ln_choice:
                    found = True
                    str(c)
                    modify_contact(c)
            contacts.sort()
            if not found:
                print("Contact not found.")
        elif choice == 5:
        # Save and Quit
            repeat = False
            write_file(contacts)
            print("Saving File...\nEnding Program")

main()  