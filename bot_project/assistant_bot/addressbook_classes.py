from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)
        
            

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y") 
            super().__init__(value) 
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")     
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_rm = self.find_phone(phone)
        if phone_rm:
            self.phones.remove(phone_rm)
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone, new_phone):
       phone_to_edit = self.find_phone(old_phone)
       if phone_to_edit:
           self.add_phone(new_phone)
           self.remove_phone(old_phone)
       else:
           raise ValueError("Old phone number not found.")
    
    def add_birthday(self, birthday_str):  
        self.birthday = Birthday(birthday_str)
        

    def __str__(self):
        phones_str = ', '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"
    
      

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name {name} not found.")
        
    def __str__(self):
        if not self.data:
            return "The contact list is empty."
        return "\n".join(str(record) for record in self.data.values())
    
    def get_upcoming_birthdays(self, days = 7):
        upcoming = []
        today = date.today()
        
        for record in self.data.values():
            if not record.birthday:
                continue
            bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            bday = bday.replace(year=today.year)
            
            if bday < today:
                bday = bday.replace(year = today.year + 1)
                
            days_diff = (bday - today).days 
            
            if 0 <= days_diff <=days:
                if bday.weekday() >= 5:
                    shift = 7 - bday.weekday()
                    bday += timedelta(days = shift)
                    
                upcoming.append({
                    "name": record.name.value,
                    "birthday": bday.strftime("%d.%m.%Y") 
                })
        return upcoming