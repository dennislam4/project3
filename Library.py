# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-03-2022
# Description: Library simulator with different classes that represent the patron, library items, and the library
# itself . Books, albums, and movies are the three classes that are inherited from the LibraryItem class to represent
# the items that the library contains.

class LibraryItem:
    """Class that represents items found within the library"""
    def __init__(self, library_item_id, title):
        """Initilizes LibraryItem class"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._requested_by = None
        self._checked_out_by = None
        self._check_out_length = 0

    def get_library_item_id(self):
        """Get method for unique identifier for a LibraryItem"""
        return self._library_item_id

    def get_location(self):
        """Get method for LibraryItem's location"""
        return self._location

    def get_title(self):
        """Get method for LibraryItem title"""
        return self._title

    def get_date_checked_out(self):
        """Get method for LibraryItem check out date"""
        return self._date_checked_out

    def get_requested_by(self):
        """Get method for LibraryItem request from patron"""
        return self._requested_by

    def get_checked_out_by(self):
        """Get method for LibraryItem check out from patron"""
        return self._checked_out_by

    def get_check_out_length(self):
        """Returns check_out_length"""
        return self._check_out_length

    def set_location(self, location):
        """Set method for location of LibraryItem."""
        self._location = location

    def set_date_checked_out(self, check_out_date):
        """Set method for LibraryItem check out date"""
        self._date_checked_out = check_out_date

    def set_requested_by(self, patron):
        """Set method for LibraryITem request by patron"""
        self._requested_by = patron

    def set_checked_out_by(self, patron):
        """Set method for LibraryItem check out by patron"""
        self._checked_out_by = patron


class Book(LibraryItem):
    """Represents a book that is inherited from LibraryItem"""
    def __init__(self, library_item_id, title, author):
        """Initilizes Book class"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_check_out_length(self):
        """Returns check out length of Book"""
        check_out_length = 21
        return check_out_length

    def get_author(self):
        """Returns author of Book"""
        return self._author


class Album(LibraryItem):
    """Represents an album that is inherited from LibraryItem"""
    def __init__(self, library_item_id, title, artist):
        """Initilizes Album class"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_check_out_length(self):
        """Returns check out length of Album"""
        check_out_length = 14
        return check_out_length

    def get_artist(self):
        """Get method for artist"""
        return self._artist


class Movie(LibraryItem):
    """Represents a movie that is inherited from LibraryItem"""
    def __init__(self, library_item_id, title, director):
        """Initilizes Movie class"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_check_out_length(self):
        """Returns check out length of Movie"""
        check_out_length = 7
        return check_out_length

    def get_director(self):
        """Returns director"""
        return self._director


class Patron:
    """Class that represents a Patron and their fees and checkouts of library items"""
    def __init__(self, name, patron_id):
        """Initializes Patron class"""
        self._name = name
        self._patron_id = patron_id
        self._checked_out_items = []
        self._fine_amount = 0

    def get_name(self):
        """Returns patron's name"""
        return self._name

    def get_patron_id(self):
        """Returns patron's id number"""
        return self._patron_id

    def get_checked_out_items(self):
        """Returns the list of LibraryItems checked out by Patron"""
        return self._checked_out_items

    def get_fine_amount(self):
        """Returns the fine amount issued to patron"""
        return self._fine_amount

    def add_library_item(self, library_item):
        """Adds library item to list of checked_out_items by appending them, returns the list afterwards"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes library item from list of checked_out_items by remove(), returns the list afterwards"""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, fine):
        """Adds or subtracts fine based on its sign, to fine_amount issued to patron"""
        self._fine_amount += fine


class Library:
    """Class that represents the Library """
    def __init__(self):
        """Initializes current date as well as holdings and member collections as empty lists"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """Returns holdings"""
        return self._holdings

    def get_members(self):
        """Returns members"""
        return self._members

    def get_current_date(self):
        """Returns the current date as an integer counting days"""
        return self._current_date

    def add_library_item(self, library_item):
        """Adds library items to holdings"""
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """Adds a patron to members"""
        self._members.append(patron)

    def lookup_library_item_from_id(self, library_item_id):
        """Returns library item based on id associated with library item"""
        for library_item in self._holdings:
            if library_item.get_library_item_id() == library_item_id:
                return library_item
        return None

    def lookup_patron_from_id(self, patron_id):
        """Returns the patron id based on the id parameter"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """
        Checks for Patron's ID to see if they are in the members' collection, returns patron not found if they are not
        within the members holdings. Then, checks for library item ID and either returns the item is not found, item is
        already checked out, or item is on hold from another patron depending on item status.
        """

        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        library_item = self.lookup_library_item_from_id(library_item_id)
        if not library_item:
            return "item not found"

        item_location = library_item.get_location()
        if item_location == "CHECKED_OUT":
            return "item already checked out"
        elif item_location == "ON_HOLD_SHELF":
            return "item on hold by other patron"
        else:
            library_item.set_location("CHECKED_OUT")
            library_item.set_checked_out_by(patron)
            library_item.set_date_checked_out(self._current_date)
            patron.add_library_item(library_item)

            if library_item.get_requested_by() == patron:
                library_item.set_requested_by(None)
            return "check out successful"

    def return_library_item(self, library_item_id):
        """
        Checks for LibraryItem in holdings collection and returns wether or not the item is already in the list or not.
        Updates Patron's checked out items and adds returned library item to the holdings list.
        """
        id_lookup = self.lookup_library_item_from_id(library_item_id)
        for library_items in self._holdings:
            if library_items.get_library_item_id() == library_item_id:
                if id_lookup.get_location() != "CHECKED_OUT":
                    return "item already in library"
                if id_lookup.get_location() == "CHECKED_OUT":
                    patron = library_items.get_checked_out_by()
                    patron.remove_library_item(library_items)
                    library_items.set_checked_out_by(None)
                    if library_items.get_requested_by() is not None:
                        library_items.set_location("ON_HOLD_SHELF")
                    else:
                        library_items.set_location("ON_SHELF")
                    return "return successful"
        return "item not found"

    def request_library_item(self, patron_id,  library_item_id):
        """
        Checks for patron's ID and the library ID then returns wether or not item is in Library's holdings. Returns
        wether or not patron was found or the library item was found in Library's holdings. Updates library's requests
        and returns request successful.
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        library_item = self.lookup_library_item_from_id(library_item_id)
        item_location = library_item.get_location()
        if item_location == "ON_HOLD_SHELF":
            return "item already on hold"
        elif item_location == "CHECKED_OUT":
            return "item not found"
        else:
            library_item.set_location("ON_HOLD_SHELF")
            library_item.set_requested_by(patron)
            return "request successful"

    def pay_fine(self, patron_id, amount_in_dollars):
        """
        Checks for patron ID and returns the fine amount that is being paid. Returns either if the patron is found
        matching the ID or the fine is amended and returns that the payment was successful.
        """
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                patron.amend_fine(-1 * amount_in_dollars)
                return "payment successful"
        return "patron not found"

    def increment_current_date(self):
        """
        Increments the current day by 1 and increases Patron's fine amount by 10 cents for each overdue LibraryItem that
        they have checked out.
        """
        self._current_date += 1
        for patron in self._members:
            for library_item in patron.get_checked_out_items():
                date_checked_out = library_item.get_date_checked_out()
                library_item_check_out_length = library_item.get_check_out_length()

                if date_checked_out + library_item_check_out_length < self._current_date:
                    patron.amend_fine(0.10)


# def main():
#     b1 = Book("345", "Phantom Tollbooth", "Juster")
#     b2 = Book("456", "blah", "boop")
#
#     print(b1.get_author())
#     print(b2.get_author())
#
#     p1 = Patron("Felicity", "abc")
#     p2 = Patron("Waldo", "bcd")
#
#     lib = Library()
#     lib.add_library_item(b1)
#     lib.add_library_item(b2)
#     lib.add_patron(p1)
#     lib.add_patron(p2)
#
#     for _ in range(7):
#         lib.increment_current_date()  # 7 days pass
#     lib.check_out_library_item("bcd", "456")
#     for _ in range(28):
#         lib.increment_current_date()  # 28 days pass
#     p2_fine = p2.get_fine_amount()
#     print(p2_fine)
#     lib.pay_fine("bcd", p2_fine + 1.0)
#     lib.return_library_item("456")
#     p2_fine = p2.get_fine_amount()
#     print(p2_fine)
#

if __name__ == '__main__':
    main()
