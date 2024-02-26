student_marks = input("enter marks separated by coma\n").split(",")
for i in range(0,len(student_marks)):
    student_marks[i] = int(student_marks[i])
max = 0
for i in student_marks:
    if (i>max):
        max = i
print("height score in the class is ",max)