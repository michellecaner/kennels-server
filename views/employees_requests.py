EMPLOYEES = [
    {
      "id": 1,
      "name": "Justin Case"
    },
    {
      "id": 2,
      "name": "Irma Gawd"
    },
    {
      "id": 3,
      "name": "Paige Turner"
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
