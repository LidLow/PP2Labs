import SQL

def mainMenu():
    while True:
        print("\n=== PHONEBOOK MENU ===")
        print("1. Show all contacts")
        print("2. Show contacts ordered by a field")
        print("3. Add a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Clear all contacts")
        print("7. Import a CSV")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            SQL.showContacts()
        elif choice == "2":
            PREPshowOrderedContacts()
        elif choice == "3":
            PREPcreateContact()
        elif choice == "4":
            PREPupdateContact()
        elif choice == "5":
            PREPdeleteContact()
        elif choice == "5":
            PREPdeleteContact()
        elif choice == "6":
            confirm = input("Are you sure? This will DELETE ALL contacts. (yes/no): ").lower()
            if confirm == "yes":
                SQL.clearContacts()
                print("All contacts have been deleted.")
            else:
                print("Operation canceled.")
        elif choice == "7":
            SQL.importCSV()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def PREPupdateContact():
    id = input("ID: ")
    first_name = input("First name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone number: ")
    SQL.updateContact(id, first_name, last_name, phone_number)

def PREPcreateContact():
    first_name = input("First name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone number: ")
    SQL.createContact(first_name, last_name, phone_number)

def PREPshowOrderedContacts():
    print("Order by:\n 1) first name\n 2) last name\n 3) phone number")

    while(True):
        selection = input("ENTER: ")

        if selection == "1":
            key = "first_name"
            break
        elif selection == "2": 
            key = "last_name"
            break
        elif selection == "3": 
            key = "phone_number"
            break
        else:
            continue

    print("\nOrder by:\n 1) Ascending\n 2) Descending")

    while(True):
        selection = input("Order by: ")

        if selection == "1":
            order = "ASC"
            break
        elif selection == "2": 
            order = "DESC"
            break
        else:
            continue
    
    SQL.showOrderedContacts(key, order)

def PREPdeleteContact():
    name = input("First name or last name: ")
    SQL.deleteContact(name)

if __name__ == "__main__":
    mainMenu()