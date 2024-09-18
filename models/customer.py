class Customer:
    def _init_(self, name):
        self.name = name  # Use the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def _repr_(self):
        return f"Customer(name={self.name!r})"