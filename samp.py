employee = [
    [3, "Brad"],
    [1, "John"],
    [2, "Dan"]
]

bonus = {
    2: 500,
    4: 2000
}

for emp_id, name in employee:
    if emp_id not in bonus or bonus[emp_id] < 1000:
        print(name, bonus.get(emp_id))
