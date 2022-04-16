LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "500 Puppy Way"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    }
  ]

def get_all_locations():
    """This function returns all locations"""
    return LOCATIONS

def get_single_location(id):
    """This function returns a single location"""
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location
  