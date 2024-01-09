class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit, sub_teacher):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.sub_teacher = sub_teacher
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)


# instance
student1 = Student("405", "Alice")
student2 = Student("261", "Nut")
student3 = Student("656", "Toey")
student4 = Student("345", "Mook")
student5 = Student("085", "Ink")

student = [student1, student2, student3, student4, student5]

teacher1 = Teacher("101666", "Jirasak")
teacher2 = Teacher("906835", "Thananchai")
teacher3 = Teacher("589009", "Sakchai")

teacher = [teacher1, teacher2, teacher3]

subject1 = Subject("01076140", "OOP", "1", "3", teacher[0])
subject2 = Subject("90678910", "OOP", "2", "3", teacher[1])
subject3 = Subject("45889109", "CAL", "3", "3", teacher[2])

subject1.add_student(student1)
subject1.add_student(student2)
subject2.add_student(student3)
subject2.add_student(student4)
subject3.add_student(student5)
# print(subject1.student_list)

subject = [subject1, subject2, subject3]
"""
def get_student(teacher_id):
    for sj in subject:
        if teacher_id == sj.sub_teacher.teacher_id:
            print(sj.section)
            
get_student('906835')
"""

def get_students(teacher_id):
    for sj in subject:
        if teacher_id == sj.sub_teacher.teacher_id:
            students = [student.student_name for student in sj.student_list]
            return(f"Students studying with teacher {teacher_id}: {', '.join(students)}")

print(get_students("906835"))

def get_subjects(student_id):
    subjects_studied = []
    for sj in subject:
        for student in sj.student_list:
            if student_id == student.student_id:
                subjects_studied.append(sj.subject_name)
                return(f"Subjects studied by student {student_id}: {', '.join(subjects_studied)}")

print(get_subjects("261"))