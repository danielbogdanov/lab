from datetime import datetime
from os import get_terminal_size

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        if self.expires < NOW:
            eturn False
        else:
            return True

    @expired.setter
    def expired(self, value):
        if isinstance(value, bool):
            self.expires = NOW if value else self.expires
        else:
            raise ValueError("expired must be a boolean value")

    
    
    
