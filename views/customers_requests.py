CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "987 Peanut Drive",
      "phone": "615-987-6543",
      "email": "syd@noh.com",
      "animalId": 1
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Lane",
      "phone": "615-987-6543",
      "email": "trevor@guinn.com",
      "animalId": 2
    },
    {
      "id": 3,
      "name": "Michelle Caner",
      "address": "333 Witch Way",
      "phone": "718-333-9999",
      "email": "michelle@caner.com",
      "animalId": 3
    },
    {
      "id": 4,
      "name": "Joe Schmoe",
      "address": "1212 Count Court",
      "phone": "212-555-1212",
      "email": "joe@schmoe.com",
      "animalId": 4
    }
]

def get_all_customers():
    """This function returns all customers"""
    return CUSTOMERS

def get_single_customer(id):
    """This function returns a single customer"""
    requested_customer = None
  
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
         
    return requested_customer
