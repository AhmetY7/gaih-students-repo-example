studentsGrades = {"student1_passingGrade":0, "student2_passingGrade":0, "student3_passingGrade": 0, "student4_passingGrade":0, "student5_passingGrade":0}
gradesList = list()
i=0
for key,value in studentsGrades.items():
    print(f'{i+1}. Student Grades')
    studentsGrades[key] = (int(input("Midterm Grade:")) * 0.3) + (int(input("Project Grade:")) * 0.3) + (int(input("Final Grade:")) * 0.4)
    gradesList.append(studentsGrades[key])
    i += 1

gradesList.sort(reverse=True)
print(gradesList)
