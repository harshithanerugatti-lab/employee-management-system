with open("employees.txt", "r") as file:
    for line in file:
        employee_id, name, department = line.strip().split(", ")
        print(f"ID: {employee_id}, Name: {name}, Department: {department}")