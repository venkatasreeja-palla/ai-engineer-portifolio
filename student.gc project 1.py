name = input("Enter student name: ")

subjects = ["Telugu", "Hindi", "English", "Maths", "Science", "Social"]
marks = []

for subject in subjects:
    mark = int(input("Enter" + "subject" + "marks:"))
    marks.append(mark)

total = sum(marks)
average = total/6

print("\n---Student Report---")
print("Student name:", name)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    Grade = "A"
elif average >= 75:
    Grade = "B"
elif average >= 60:
    Grade = "C"
elif average >= 40:
    Grade = "D"
else:
    Grade = "Fail"

print("Grade:", Grade)


if all(mark >= 35 for mark in marks):
    print("Result:PASS")
else:
    print("Result:FAIL")
