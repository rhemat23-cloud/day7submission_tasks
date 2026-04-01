# Example dataset: list of dictionaries
students = [
    {"name": "unik", "age": 20, "grade": "A"},
    {"name": "unish", "age": 22, "grade": "B"},
    {"name": "utin", "age": 19, "grade": "A"},
    {"age": 21, "grade": "C"}  
]

# Function to safely extract the 'name' field
def get_name(student):
    # Validate that input is a dictionary and has a 'name' key
    if isinstance(student, dict) and "name" in student:
        return student["name"]
    return None  # Return None if name is missing

# Use map() to transform the list
names = list(map(get_name, students))

# Filter out None values (students without names)
names = [name for name in names if name is not None]

print("Student Names:", names)

