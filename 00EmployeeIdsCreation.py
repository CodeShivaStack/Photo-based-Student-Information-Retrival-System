valid_emp_ids = ["102", "103", "107", "10342", "102221","102224","103421","102849"]

with open("valid_emp_ids.txt", "w") as file:
    for emp_id in valid_emp_ids:
        file.write(emp_id + "\n")