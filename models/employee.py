class Employee():
    """Creates a new object in the Employee class"""
    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.location = None

new_employee = Employee(4, "Nat E. Ice", "333 Beer St", 2)
    