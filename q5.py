def main():
    students = [
    {"name": "Alice", "course": "Data Science", "attendance": 85},
    {"name": "Bob", "course": "Web Dev", "attendance": 90},
    {"name": "Charlie", "course": "Data Science", "attendance": 78},
    {"name": "David", "course": "Data Science", "attendance": 92},
]
    result =[]
    for student in students:
        if student["course"] == "Data Science" and student["attendance"] > 80:
            result.append(student)
    print(f"The registered Students are: {result}")
if __name__ == "__main__":
    main()