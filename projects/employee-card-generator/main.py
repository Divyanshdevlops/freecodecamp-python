def create_employee_card(name, position, employee_id):
    print("=" * 40)
    print("         EMPLOYEE CARD")
    print("=" * 40)
    print(f"Name:        {name}")
    print(f"Position:    {position}")
    print(f"Employee ID: {employee_id}")
    print("=" * 40)


name = input("Enter employee name: ")
position = input("Enter employee position: ")
employee_id = input("Enter employee ID: ")

create_employee_card(name, position, employee_id)
