class Customer():
    """Creates a new object in the Customer class"""
    def __init__(self, id, first_name, last_name, email, new_customer):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.new_customer = new_customer

new_client = Customer(5, "Sally", "Kato", "skato@gmail.com", True)
    