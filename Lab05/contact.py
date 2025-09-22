# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 22, 2025

class Contact:
    def _init__(self, fn, ln, ph, addr, city, zip):
        self.fn = fn
        self.ln = ln
        self.ph = ph
        self.addr = addr
        self.city = city
        self.zip = zip

    def __lt__(self, other):
        if self.ln == other.ln:
            return self.fn < self.ln
        return self.ln < other.ln

    def __str__(self):
        return (f"{self.f_name} {self.l_name}\n"
                f"{self.phone}\n"
                f"{self.address}\n"
                f"{self.city}, {self.zip}")

    def __repr__(self):
        return f"{self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}"