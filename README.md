# Object-Oriented Programming Assignment

A Python assignment focused on creating a `Student` class and practicing object-oriented programming alongside lists, dictionaries, sets, and tuples.

## Features

- Create student objects with a name, email, and list of grades.
- Add grades, calculate averages, and display student information.
- Store students in a dictionary using their emails as keys.
- Retrieve students safely with dictionary `.get()`.
- Use a set to display unique grades across all students.
- Convert grades to tuples and demonstrate immutability with exception handling.
- Practice removing, accessing, and counting list items.

## Student Class

| Method | Purpose |
| --- | --- |
| `add_grade(grade)` | Adds a grade to the student's grades list. |
| `average_grade()` | Returns the average of the student's grades. |
| `display_info()` | Prints the student's name, email, and grades. |
| `grades_tuple()` | Returns the student's grades as a tuple. |

## Program Flow

1. Create three students with different names, emails, and initial grades.
2. Add two new grades to each student and display their information and averages.
3. Build `student_dict` and use `get_student_by_email(email)` to look up students.
4. Display the unique grades using a set.
5. Attempt to change a tuple value and handle the exception using `try/except`.
6. Remove each student's last grade with `.pop()`.
7. Display each student's first grade, last grade, and total number of grades using `len()`.

## How to Run

Install Python 3, download or clone the repository, and open a terminal in the project folder. Run:

```bash
python3 ct_python_assignment.py
```

This command assumes the file is named `ct_python_assignment.py`. If your filename differs, use that filename instead. For filenames containing parentheses or spaces, wrap the filename in quotes.

No external packages are needed. Email validation uses Python’s built-in `re` module.

## Bonus Features

- Validates email formatting using a regular expression that checks for a `.com` ending.
- Includes a loop intended to count grades above 90 after the last grade has been removed from each student.

## Known Issue

The grade counter currently uses `count =+ 1`, which assigns positive 1 instead of increasing the count. Change it to `count += 1` to count correctly. With the current sample data, the corrected total after removing the last grades is 4.

## Concepts Practiced

Python classes, objects, attributes, methods, collection types, loops, indexing, regular expressions, and exception handling.

The current implementation stores each student’s grades in `self.grade` (singular).

## Author

Matthew Shin


