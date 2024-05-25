def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input, please try again."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def phone(args, contacts):
    name = args.strip()
    return contacts[name]

def show_all(args, contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    commands = {
        "add": add_contact,
        "phone": phone,
        "all": show_all
    }

    while True:
        user_input = input("Enter a command: ").strip().lower()
        if user_input in commands:
            command = commands[user_input]
            args = input("Enter the argument for the command: ").strip()
            print(command(args, contacts))
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
