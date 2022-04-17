class Employee():
    """Creates a new object in the Employee class"""
    def __init__(self, id, name, role, location):
        self.id = id
        self.name = name
        self.role = role
        self.location_id = location

new_employee = Employee(4, "Nat E. Ice", "staff", 2)
    