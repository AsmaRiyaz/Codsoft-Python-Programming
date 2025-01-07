import json

# File to store contact data
DATA_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the data file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    """Save contacts to the data file."""
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    """View all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    query = input("Enter name or phone number to search: ").lower()
    contacts = load_contacts()

    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    if not results:
        print("No matching contacts found.")
        return

    print("\nSearch Results:")
    for contact in results:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").lower()
    contacts = load_contacts()

    for contact in contacts:
        if contact['name'].lower() == name:
            print("Enter new details (leave blank to keep current):")
            contact['name'] = input(f"Name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load_contacts()

    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").lower()
            if confirm == "yes":
                contacts.pop(i)
                save_contacts(contacts)
                print("Contact deleted successfully!")
                return

    print("Contact not found.")

def main_menu():
    """Main menu for the Contact Book application."""
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
