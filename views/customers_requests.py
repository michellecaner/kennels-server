import sqlite3
import json
from models import Customer


CUSTOMERS = [
     {
        "id": 1,
        "first_name": "Mame",
        "last_name": "Burnside",
        "email": "mburnside@gmail.com",
        "new_customer": True
    },
    {
        "id": 2,
        "first_name": "Patrick",
        "last_name": "Dennis",
        "email": "pdennis@gmail.com",
        "new_customer": True
    },
    {
        "id": 3,
        "firs_name": "Agnes",
        "last_name": "Gooch",
        "email": "agooch@gmail.com",
        "ne_customer": True
    },
    {
        "id": 4,
        "first_name": "Vera",
        "last_name": "Charles",
        "email": "vcharles@gmail.com",
        "new_customer": True
    }
]

def get_all_customers():
    """This function gets all the customers"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)

def get_single_customer(id):
    """This function gets a single customer"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

        return json.dumps(customer.__dict__)

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

def get_customers_by_email(email):
    """This function allows users to search customers by email."""

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)