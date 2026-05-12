# MapReduce program to find grades of students

with open("Big Data Analytics\StudentGrade\students.txt", "r") as file:
    lines = file.readlines()

print("Student Grades:")
print("----------------")

for line in lines:
    name, marks = line.split()
    marks = int(marks)

    # Grade logic
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(name, ":", grade)