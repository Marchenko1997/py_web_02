import pickle
import os 
from assistant_bot.addressbook_classes import AddressBook

FILENAME = "assistant_bot/addressbook.pkl"

def save_data(book: AddressBook, filename: str = FILENAME):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = FILENAME) -> AddressBook:
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return AddressBook() 