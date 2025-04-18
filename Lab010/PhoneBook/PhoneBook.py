import psycopg2
import csv
from config import load_config

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
            showContacts()
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
                clearContacts()
                print("All contacts have been deleted.")
            else:
                print("Operation canceled.")
        elif choice == "7":
            importCSV()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    

def PREPcreateContact():
    first_name = input("First name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone number: ")
    createContact(first_name, last_name, phone_number)

def createContact(first_name, last_name, phone_number):
    SQL = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s) ON CONFLICT (phone_number) DO NOTHING;"
    config = load_config()

    try: 
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (first_name, last_name, phone_number))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def showContacts():
    SQL = "SELECT * FROM contacts;"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL)

            row = curs.fetchone()
            while row is not None:
                print(row)
                row = curs.fetchone()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)


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
    
    showOrderedContacts(key)

def showOrderedContacts(key):
    SQL = "SELECT * FROM contacts ORDER BY %s"
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
                curs.execute(SQL, (key))

                print("\nYour Contacts:", curs.rowcount)

                row = curs.fetchone()
                while row is not None:
                    print(row)
                    row = curs.fetchone()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)


def PREPdeleteContact():
    id = input("ID: ")
    deleteContact(id)

def deleteContact(id):
    SQL = "DELETE FROM contacts WHERE id=%s;"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (id))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        return Error


def clearContacts():
    config = load_config()
    SQL = "TRUNCATE TABLE contacts;"

    try: 
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def PREPupdateContact():
    id = input("ID: ")
    first_name = input("First name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone number: ")
    updateContact(id, first_name, last_name, phone_number)

def updateContact(id, first_name, last_name, phone_number):
    SQL = "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s WHERE id=%s;"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (first_name, last_name, phone_number, id))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        return Error

#################################################################################################

def importCSV():
    path = input("Directory of the CSV: ")

    with open(rf"{path}", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            createContact(row[0], row[1], row[2])


if __name__ == "__main__":
    mainMenu()