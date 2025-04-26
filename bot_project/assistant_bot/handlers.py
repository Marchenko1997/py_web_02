from assistant_bot.utils import input_error  
from assistant_bot.data import book
from assistant_bot.addressbook_classes import Record

@input_error
def add_contact(args, book):
    name, phone, *_ = args 
    record = book.find(name)
    message = "Contact updated." 
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added." 
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone  = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.edit_phone(old_phone, new_phone)
    return f"Phone number for '{name}' updated."
   

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found"
    return f"Phone numbers for {name}: {', '.join(p.value for p in record.phones)}"


@input_error
def show_all(book):
    if not book:
        return "The contact list is empty."
    return str(book)

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthday)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        return "Birthday not found."
    return f"{name}'s birthday: {record.birthday.value}"


@input_error
def birthdays(args = None, book = None):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    result = []
    for entry in upcoming:
        result.append(f"{entry['name']} : {entry['birthday']}")
    return "\n".join(result)	



@input_error
def handle_command(command, args, book):
    commands = {
        "hello": lambda *_, **__: "How can I help you?",
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
    }
    handler = commands.get(command)
    if handler:
        return handler(args, book) if args else handler(book = book)
    return "Invalid command. Please try again."