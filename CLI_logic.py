from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(self.__validate_phone(value))

    def __validate_phone(self, value) -> str | None:
        if len(value.strip()) == 10 and value.strip().isdigit():
            return value.strip()
        else:
            raise ValueError("Phone number not valid")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj is not None:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str) -> ValueError | None:
        # phone_obj = self.find_phone(old_phone)
        # if phone_obj is not None:
        #     for i, x in enumerate(self.phones):
        #         if x == phone_obj:
        #             self.phones[i] = Phone(new_phone)
        if self.find_phone(old_phone) is not None:
            try:
                self.add_phone(new_phone)
            except ValueError as e:
                raise e
            else:
                self.remove_phone(old_phone)
        return None

    def find_phone(self, find_phone: str) -> Phone | None:
        for phone in self.phones:
            if phone.value == find_phone:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        self.data.get(name)

    def delete(self, name: str) -> None:
        record_obj = self.find(name)
        if record_obj is not None:
            del self.data[record_obj.name.value]

    def __str__(self):
        if not self.data:
            return "Адресна книга порожня."

        lines = ["=== Адресна книга ==="]
        for record in self.data.values():
            lines.append(f"  • {record}")

        return "\n".join(lines)


def main():
    book = AddressBook()

    john_record = Record("John")

    john_record.add_phone("5555555555")
    john_record.add_phone("   1234561234")

    john_record.remove_phone("5555555555")
    john_record.add_phone("5555555555")

    try:
        john_record.edit_phone("5555555555", "1234569]76")
    except Exception as e:
        print(f"Викликається виняток: {e}")

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    book.add_record(john_record)
    book.add_record(jane_record)

    print(book)


if __name__ == "__main__":
    main()
