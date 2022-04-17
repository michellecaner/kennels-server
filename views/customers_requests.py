CUSTOMERS = [
     {
        "id": 1,
        "first name": "Mame",
        "last name": "Burnside",
        "email": "mburnside@gmail.com",
        "new customer": True
    },
    {
        "id": 2,
        "first name": "Patrick",
        "last name": "Dennis",
        "email": "pdennis@gmail.com",
        "new customer": True
    },
    {
        "id": 3,
        "first name": "Agnes",
        "last name": "Gooch",
        "email": "agooch@gmail.com",
        "new customer": True
    },
    {
        "id": 4,
        "first name": "Vera",
        "last name": "Charles",
        "email": "vcharles@gmail.com",
        "new customer": True
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

def create_customer(customer):
    """This function creates a new customer"""
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    """This function deletes a single customer"""
    customer_index = -1

    for index, customer in enumerate (CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """This function deletes AND replaces customer with updated info"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
