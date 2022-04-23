class Customer():
    """Creates a new object in the Customer class"""
    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

new_client = Customer(5, "Sally Kato", "42 Taco Way", "skato@gmail.com", "secret123")
    