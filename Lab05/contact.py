# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 22, 2025

class Contact:
    def __init__(self, fn, ln, ph, addr, city, zip):
        """ 
        Constructor for the Contact class

        Args:
            self, fn, ln, ph, addr, city, zip: attributes of the Contact class

        Returns: 
            None 
        """
        self.fn = fn
        self.ln = ln
        self.ph = ph
        self.addr = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        """ 
        Passes in two contacts and compares them by last names, if they are the same, then compare by first names.

        Args:
            self, other: Two Contacts to be compared and sorted

        Returns: 
            A boolean value that is true if the two contacts are the same and false otherwise
        """
        if self.ln == other.ln:
            return self.fn < self.ln
        return self.ln < other.ln

    def __str__(self):
        """ 
        A method to print the contact.

        Args:
            self: The Contact to be printed

        Returns: 
            A string that is used to display the contact to the console
        """
        return (f"{self.fn} {self.ln}\n"
                f"{self.ph}\n"
                f"{self.addr}\n"
                f"{self.city}, {self.zip}")

    def __repr__(self):
        """ 
        A method to format the contact to be written to the file.

        Args:
            self: The Contact to be formatted and written

        Returns: 
            A string that is used to write the contact to the file
        """ 
        return f"{self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}"