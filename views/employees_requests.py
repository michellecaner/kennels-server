EMPLOYEES = [
    {
      "id": 1,
      "name": "Justin Case",
      "role": "staff",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Irma Gawd",
      "role": "staff",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Paige Turner",
      "role": "staff",
      "locationId": 1
    }
]

def get_all_employees():
    """This function returns all employees"""
    return EMPLOYEES

def get_single_employee(id):
    """This function returns a single employee"""
    requested_employee = None
 
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
        
    return requested_employee

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

