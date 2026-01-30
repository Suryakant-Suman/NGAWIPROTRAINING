import json
import csv
import os

# ================= CLASSES =================
class Student:
    def __init__(self, sid, name, dept, sem, marks):
        self.sid = sid
        self.name = name
        self.dept = dept
        self.sem = sem
        self.marks = marks

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 85:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        else:
            grade = "C"
        return avg, grade

    def to_dict(self):
        avg, grade = self.calculate_performance()
        return {
            "id": self.sid,
            "name": self.name,
            "department": self.dept,
            "semester": self.sem,
            "marks": self.marks,
            "average": round(avg, 2),
            "grade": grade
        }

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


class Faculty:
    def __init__(self, fid, name, dept, salary):
        self.fid = fid
        self.name = name
        self.dept = dept
        self.salary = salary


class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# ================= FILE HANDLING =================
def save_students_json(students):
    with open("students.json", "w") as f:
        json.dump([s.to_dict() for s in students.values()], f, indent=2)
    print("✔ JSON file created: students.json")


def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Semester", "Average", "Grade"])
        for s in students.values():
            avg, grade = s.calculate_performance()
            writer.writerow([s.sid, s.name, s.dept, s.sem, round(avg, 2), grade])
    print("✔ CSV file created: students_report.csv")


# ================= MAIN =================
students = {}
faculty = {}
courses = {}

while True:
    print("\n===== SMART UNIVERSITY MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Enroll Student to Course")
    print("5. Calculate Student Performance")
    print("6. Compare Two Students")
    print("7. Generate CSV & JSON Reports")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # -------- OPTION 1 --------
    if choice == "1":
        sid = input("Enter Student ID: ")
        if sid in students:
            print("Error: Student ID already exists")
            continue
        name = input("Enter Student Name: ")
        dept = input("Enter Department: ")
        sem = int(input("Enter Semester: "))
        marks = list(map(int, input("Enter 5 Marks (space separated): ").split()))
        students[sid] = Student(sid, name, dept, sem, marks)
        print("Student Created Successfully")

    # -------- OPTION 2 --------
    elif choice == "2":
        fid = input("Enter Faculty ID: ")
        name = input("Enter Faculty Name: ")
        dept = input("Enter Department: ")
        salary = int(input("Enter Monthly Salary: "))
        faculty[fid] = Faculty(fid, name, dept, salary)
        print("Faculty Created Successfully")

    # -------- OPTION 3 --------
    elif choice == "3":
        code = input("Enter Course Code: ")
        cname = input("Enter Course Name: ")
        credits = int(input("Enter Credits: "))
        fid = input("Enter Faculty ID: ")
        courses[code] = Course(code, cname, credits, faculty[fid])
        print("Course Added Successfully")

    # -------- OPTION 4 --------
    elif choice == "4":
        sid = input("Enter Student ID: ")
        code = input("Enter Course Code: ")
        print("Enrollment Successful")
        print("Student Name:", students[sid].name)
        print("Course Name :", courses[code].name)

    # -------- OPTION 5 --------
    elif choice == "5":
        sid = input("Enter Student ID: ")
        avg, grade = students[sid].calculate_performance()
        print("\nStudent Performance Report")
        print("--------------------------")
        print("Name   :", students[sid].name)
        print("Marks  :", students[sid].marks)
        print("Average:", round(avg, 2))
        print("Grade  :", grade)

    # -------- OPTION 6 --------
    elif choice == "6":
        s1 = input("Enter First Student ID: ")
        s2 = input("Enter Second Student ID: ")
        print("\nComparing Students Performance")
        print("--------------------------------")
        print(students[s1].name, ">", students[s2].name, ":", students[s1] > students[s2])

    # -------- OPTION 7 --------
    elif choice == "7":
        save_students_json(students)
        generate_csv_report(students)

    # -------- OPTION 8 --------
    elif choice == "8":
        print("Thank you for using Smart University Management System")
        break

    else:
        print("Invalid Option. Try Again.")
