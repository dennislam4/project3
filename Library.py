# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-03-2022
# Description: Library simulator with different classes that represent the patron, library items, and the library itself.
# Books, albums, and movies are the three classes that are inherited from the LibraryItem class to represent the items
# that the library contains.

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

    def get_library_item_id(self):
        """Get method for unique identifier for a LibraryItem"""

    def get_location(self):
        """Get method for LibraryItem's location"""
        return self._location

    def get_title(self):
        """Get method for LibraryItem title"""
        return self._title

    def get_date_check_out(self):
        """Get method for LibraryItem check out date"""
        return self._date_checked_out

    def get_requested_by(self):
        """Get method for LibraryItem request from patron"""
        return self._requested_by

    def get_checked_out_by(self):
        """Get method for LibraryItem check out from patron"""
        return self._checked_out_by

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
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._requested_by = None
        self._checked_out_by = None
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
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._requested_by = None
        self._checked_out_by = None
        self._artist = artist

    def get_check_out_length(self):
        """Returns check out length of Album"""
        check_out_length = 14
        return check_out_length

    def get_album(self):
        """Get method for artist"""
        return self._artist


class Movie(LibraryItem):
    """Represents a movie that is inherited from LibraryItem"""
    def __init__(self, library_item_id, title, director):
        """Initilizes Movie class"""
        super().__init__(library_item_id, title)
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._requested_by = None
        self._checked_out_by = None
        self._director = director

    def get_check_out_length(self):
        """Returns check out length of Movie"""
        check_out_length = 7
        return check_out_length


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
        return self._checked_out_items

    def remove_library_item(self, library_item):
        """Removes library item from list of checked_out_items by remove(), returns the list afterwards"""
        self._checked_out_items.remove(library_item)
        return self._checked_out_items

    def amend_fine(self, fine):
        """Adds or subtracts fine based on its sign, to fine_amount issued to patron"""
        if fine >= 0:
            self._fine_amount += fine
        else:
            self._fine_amount -= fine


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
        return self._holdings

    def add_patron(self, patron):
        """Adds a patron to members"""
        self._members.append(patron)
        return self._members

    



