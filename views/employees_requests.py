import sqlite3
import json
from models import Employee
from models import Location


EMPLOYEES = [
    {
      "id": 1,
      "name": "Justin Case",
      "role": "staff",
      "location_id": 2
    },
    {
      "id": 2,
      "name": "Irma Gawd",
      "role": "staff",
      "location_id": 1
    },
    {
      "id": 3,
      "name": "Paige Turner",
      "role": "staff",
      "location_id": 1
    }
]

def get_all_employees():
    """This function gets all employees."""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee e
        JOIN Location l
            ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])

            # Add the dictionary representation of the location to the animal
            employee.location = location.__dict__

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)

def get_single_employee(id):
    """This function returns a single employee."""
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
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        return json.dumps(employee.__dict__)

def create_employee(employee):
    """This function adds the new employee dictionary to the employee list"""
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    """This function deletes a single employee"""
    employee_index = -1

    for index, employee in enumerate (EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """This function deletes AND replaces employee with updated info"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
        
def get_employees_by_location(location_id):
    """This function gets employees by their location id"""

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.address,
            a.location_id
        from Employee a
        WHERE a.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
