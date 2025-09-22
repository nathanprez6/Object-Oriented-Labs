# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 22, 2025
# Description:  A program that allows the user to view, search, and modify a contact list
# made up of contact objects.

import check_input
from contact import Contact

def read_file():
    contacts = []
    with open("addresses.txt", 'r') as addresses_file:
        for line in addresses_file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                fn, ln, ph, addr, city, zip_code = parts
                contacts.append(Contact(fn, ln, ph, addr, city, zip_code))
    contacts.sort()
    return contacts

def write_file(contacts):
    with open("addresses.txt", 'w') as addresses_file:
        for contact in contacts:
            addresses_file.write(repr(contact) + "\n")

def get_menu_choice():
    menu = """
    Rolodex Menu:
    1. Display Contacts
    2. Add Contact
    3. Search Contacts
    4. Modify Contact
    5. Save and Quit"""
    print(menu)

    user_choice = check_input.get_int_range(">", 1, 5)
    return user_choice

def modify_contact(cont):
    modify_menu = """
    1. First name
    2. Last name
    3. Phone
    4. Address
    5. City
    6. Zip
    7. Save"""

    user_choice = 0

    while user_choice != 7:
        print(modify_menu)
        user_choice = check_input.get_int_range(">", 1, 7)

        if user_choice == 1:
            cont.fn = input("Enter first name: ")
        elif user_choice == 2:
            cont.ln = input("Enter last name: ")
        elif user_choice == 3:
            cont.ph = input("Enter phone: ")
        elif user_choice == 4:
            cont.addr = input("Enter address: ")
        elif user_choice == 5:
            cont.city = input("Enter city: ")
        elif user_choice == 6:
            cont.zip = input("Enter zip: ")
        elif user_choice == 7:
            break

def main():
    contacts = read_file()
    
    menu_choice = 0

    while menu_choice != 5:
        if menu_choice == 1:
            # Display contacts
            print("Number of contacts: " + len(contacts))
            for i, contact in enumerate(contacts, start = 1):
                print(f"{i}. {contact}\n")
        elif menu_choice == 2:
            # Add contact
            print("Enter new contact: ")
            fn = input("First name: ")
            ln = input("Last name: ")
            ph = input("Phone #: ")
            addr = input("Address: ")
            city = input("City: ")
            zip = input("Zip: ")
            contacts.append(Contact(fn, ln, ph, addr, city, zip))
            contacts.sort()
        elif menu_choice == 3:
            # Search contacts
            print("Search:\n1. Search by last name\n2. Search by zip")
            search_by = check_input.get_int_range(">", 1, 2)
            if search_by == 1:
                ln_to_find = input("Enter last name: ")
                for cont in contacts:
                    if ln_to_find == cont.ln:
                        str(cont)
            else:
                zip_to_find = input("Enter zip: ")
                for cont in contacts:
                    if zip_to_find == cont.zip:
                        str(cont)
        elif menu_choice == 4:
            # Modify contact
            fn_to_mod = input("Enter first name: ")
            ln_to_mod = input("Enter last name: ")
            for cont in contacts:
                if fn_to_mod == cont.fn and ln_to_mod == cont.ln:
                    str(cont)
                    modify_contact(cont)
            contacts.sort()
        elif menu_choice == 5:
            # Save and quit
            print("Saving File...")
            write_file(contacts)

    print("Ending Program")

main()