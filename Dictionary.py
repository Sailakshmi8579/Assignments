# 1. Create a dictionary with at least 5 key-value pairs (Student ID and Name)
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Emma"
}
print("\n1. Dictionary Created:", students)

# 1.1 Adding values to the dictionary
students[106] = "Frank"
print("\n1.1 After Adding Value:", students)

# 1.2 Updating values in the dictionary
students[103] = "Chris"
print("\n1.2 After Updating Value:", students)

# 1.3 Accessing a value in the dictionary
student_id = 102
print(f"\n1.3 Accessing Student with ID {student_id}: {students.get(student_id, 'Not Found')}")

# 1.4 Creating a nested dictionary
nested_students = {
    101: {"name": "Alice", "age": 20, "grade": "A"},
    102: {"name": "Bob", "age": 21, "grade": "B"},
    103: {"name": "Chris", "age": 22, "grade": "A"},
    104: {"name": "David", "age": 23, "grade": "C"},
    105: {"name": "Emma", "age": 20, "grade": "B"}
}
print("\n1.4 Nested Dictionary Created:", nested_students)

# 1.5 Accessing values from a nested dictionary
print("\n1.5 Accessing Chris's Age:", nested_students[103]["age"])

# 1.6 Printing all keys in the dictionary
print("\n1.6 Keys in Dictionary:", students.keys())

# 1.7 Deleting a value from the dictionary
del students[104]
print("\n1.7 After Deleting Student with ID 104:", students)
