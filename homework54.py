def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper

@error_handler
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command. Format: add [name] [phone]")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@error_handler
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid command. Format: change [name] [new_phone]")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise ValueError("Contact not found.")

@error_handler
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid command. Format: phone [name]")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise ValueError("Contact not found.")

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

