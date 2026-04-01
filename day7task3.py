# Sorting students by fees and faculty by salary using key in sorted()

# Define Student and Faculty as dictionaries for simplicity
students = [
    {"name": "Arun", "fees": 45000},
    {"name": "Bala", "fees": 30000},
    {"name": "Chitra", "fees": 50000},
    {"name": "Deepak", "fees": 40000}
]

faculty = [
    {"name": "Prof. Kumar", "salary": 75000},
    {"name": "Prof. Meena", "salary": 90000},
    {"name": "Prof. Ravi", "salary": 85000},
    {"name": "Prof. Anitha", "salary": 80000}
]

# Sort students by fees (ascending)
students_sorted = sorted(students, key=lambda s: s["fees"])

# Sort faculty by salary (descending)
faculty_sorted = sorted(faculty, key=lambda f: f["salary"], reverse=True)

# Display results
print("Students sorted by fees (low to high):")
for s in students_sorted:
    print(f"{s['name']} - Fees: ₹{s['fees']}")

print("\nFaculty sorted by salary (high to low):")
for f in faculty_sorted:
    print(f"{f['name']} - Salary: ₹{f['salary']}")
