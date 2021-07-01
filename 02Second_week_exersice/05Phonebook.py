contacts = {}

while True:
    command = input()
    if command.isdigit():
        for _ in range(int(command)):
            contact_to_search = input()
            if contact_to_search not in contacts:
                print(f"Contact {contact_to_search} does not exist.")
            else:
                print(f"{contact_to_search} -> {contacts[contact_to_search]}")
        break

    contact, phone_number = command.split("-")
    contacts[contact] = phone_number
