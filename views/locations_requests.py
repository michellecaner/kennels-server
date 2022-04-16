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

def create_location(location):
    """This function adds the new location dictionary to the location list"""
    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location

def delete_location(id):
    """This function deletes a single location"""
    location_index = -1

    for index, location in enumerate (LOCATIONS):
        if location["id"] == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)
