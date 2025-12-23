import json
import os


class ContactManager:
    """Class to manage a collection of contacts."""

    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self) -> dict:
        """
        Loads contacts from a JSON file.
        :return: Dictionary of contacts.
        """
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {}

    def save_contacts(self) -> None:
        """
        Saves current contacts to the JSON file.
        :return: None
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_contact(self, name, phone, email) -> None:
        """
        Adds a new contact and saves it.
        :param name: Name of new contact.
        :param phone: Phone number of the new contact.
        :param email: Email address of the new contact.
        :return: None
        """
        if name in self.contacts:
            raise ValueError(f"Contact '{name}' already exists.")

        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    def list_contacts(self) -> None:
        """
        Prints all stored contacts.
        :return: None
        """
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n--- Contact List ---")
        for name, info in self.contacts.items():
            print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")


def main():
    manager = ContactManager()

    while True:
        print("\n1. Add Contact\n2. List Contacts\n3. Exit")
        choice = input("Choose an option: ")

        match choice:
            case '1':
                 name = input("Enter name: ")
                 phone = input("Enter phone: ")
                 email = input("Enter email: ")
                 try:
                    manager.add_contact(name, phone, email)
                 except ValueError as e:
                     print(f"Error: {e}")
            case '2':
                manager.list_contacts()
            case '3':
                print("Exiting...")
                break
            case _:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
        