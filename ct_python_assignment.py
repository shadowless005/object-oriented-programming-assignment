import re


# Define a student with a name, email, and list of grades.
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    # Add a new grade to the list.
    def add_grade(self, grade):
        self.grades.append(grade)

    # Calculate the average, returning 0 if there are no grades.
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # Display student information and the average grade.
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 40)

    # Return the grades as an immutable tuple.
    def grades_tuple(self):
        return tuple(self.grades)


# Validate an email using the assignment's name@domain.com format.
def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$"
    return re.fullmatch(pattern, email) is not None


# Create three student objects with initial grades.
student1 = Student(
    "Ashley Johnson",
    "ashley@example.com",
    [86, 92, 97]
)

student2 = Student(
    "Jeremy White",
    "white@example.com",
    [95, 90, 80]
)

student3 = Student(
    "Billy Thorton",
    "billy@example.com",
    [65, 72, 79]
)

students = [student1, student2, student3]


# Add two new grades to each student.
student1.add_grade(82)
student1.add_grade(94)

student2.add_grade(100)
student2.add_grade(89)

student3.add_grade(77)
student3.add_grade(65)


# Display each student's information and average.
print("\n===== Student Information =====\n")

for student in students:
    student.display_info()


# Map each student's email to their Student object.
student_dict = {
    student.email: student
    for student in students
}


# Safely retrieve a student, returning None if not found.
def get_student_by_email(email):
    return student_dict.get(email)


print("===== Dictionary Lookup =====")

found = get_student_by_email("ashley@example.com")

if found:
    print(f"Found: {found.name}")
else:
    print("Student not found.")

print()


# Collect unique grades across all students.
unique_grades = set()

for student in students:
    unique_grades.update(student.grades)

print("===== Unique Grades =====")
print(unique_grades)
print()


# Demonstrate that tuple values cannot be changed.
print("===== Tuple Demo =====")

grades = student1.grades_tuple()
print("Tuple:", grades)

try:
    grades[0] = 100
except TypeError:
    print("Tuples are immutable. Values cannot be changed.")

print()


# Remove the last grade and display list information.
print("===== List Operations =====")

for student in students:
    student.grades.pop()

    print(student.name)
    print("First Grade:", student.grades[0])
    print("Last Grade:", student.grades[-1])
    print("Number of Grades:", len(student.grades))
    print()


# Validate each student's email.
print("===== Email Validation =====")

for student in students:
    if validate_email(student.email):
        print(f"{student.email} is Valid.")
    else:
        print(f"{student.email} is Not Valid.")

print()


# Count grades above 90 after the last grades were removed.
count = 0

for student in students:
    for grade in student.grades:
        if grade > 90:
            count += 1

print("Number of grades above 90:", count)
