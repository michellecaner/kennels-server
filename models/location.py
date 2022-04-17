class Location():
    """Creates a new object in the Location class"""
    def __init__(self, id, name, address, status):
        self.id = id
        self.name = name
        self.address = address
        self.status = status

new_location = Location(3, "Central Chattanooga", "333 Choo Choo Court", "Open for Business")
    