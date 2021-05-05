studentinfo = []
course_dict = {
    1: 'Math',
    2: 'Science',
    3: 'History'
}

while True:
    numStudents = input("How many students do you have: ")
    try:
        numStudents = int(numStudents)
    except:
        print('Invalid entry... Try using digits, ex. 1, 2, 3, etc.')
        continue
    if numStudents < 1:
        print('Please enter a valid number.')
        continue
    break

for x in range(numStudents):
    while True:
        student_name = input("Student's name: ")
        try:
            student_name = str(student_name)
        except:
            continue
        if student_name == "":
            print('Please enter a valid name.')
            continue
        break

    while True:
        student_grade = input("Student's grade: ")
        try:
            student_grade = int(student_grade)
        except:
            print('Invalid entry... Use a number grade system.')
            continue
        if student_grade > 100 or student_grade < 0:
            print('Please enter a valid grade.')
            continue
        break

    while True:
        student_course = input("Select a course -- 1.Math, 2.Science, 3.History: ")
        try:
            student_course = int(student_course)
        except:
            print('Invalid entry... try using 1, 2, or 3.')
            continue
        if student_course > 3 or student_course < 0:
            print('Please select 1, 2, or 3.')
            continue
        break
    print()

    studentinfo.append({'Name':student_name, 'Grade':int(student_grade), 'Course':int(student_course)})

for i in range(numStudents):
    print(f"Name: {studentinfo[i]['Name']}, Grade: {studentinfo[i]['Grade']}, Course: {course_dict[studentinfo[i]['Course']]}")