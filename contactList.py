
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


contacts = []


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    new_contact = Contact(name, phone)
    contacts.append(new_contact)
    print("Contact added successfully!")


def view_all_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- All Contacts ---")
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")


def search_contact():
    search_name = input("Enter the name to search for: ")
    found = False
    print("\n--- Search Results ---")
    for contact in contacts:
        if contact.name == search_name:
            print(f"Name: {contact.name}, Phone: {contact.phone}")
            found = True
    if not found:
        print("Contact not found.")


def main():
    while True:
       
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_all_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
