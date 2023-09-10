# Define a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print(f"{name} has been added to your contacts!")

# Function to list all contacts
def list_contacts():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to search for a contact by name
def search_contact():
    search_name = input("Enter the name of the contact you want to search for: ")
    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]
    if found_contacts:
        print(f"Found {len(found_contacts)} matching contacts:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No matching contacts found.")

# Main program loop
while True:
    print("\nContact Management System")
    print("1. Add a new contact")
    print("2. List all contacts")
    print("3. Search for a contact")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        list_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

