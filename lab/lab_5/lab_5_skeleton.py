class Student:
    pass


class Subject:
    pass


class Teacher:
    pass




student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id):
    pass

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    pass

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student, subject):
    pass

# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject):
    pass

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student):
    pass

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject):
    pass

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student):
    pass

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade):
    pass

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search):
    pass

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject):
    pass

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student):
    pass

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student):
    pass

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.student.student_id] = enrollment.student.student_name
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = self.search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.subject.subject_id] = enrollment.subject.subject_name
    return subject_dict

#######################################################################################

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()

# ### Test Case #1 : test enroll_to_subject complete ###
# student_enroll = list_student_enrolled_in_subject('CS101')
# print("Test Case #1 : test enroll_to_subject complete")
# print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
# print(student_enroll)
# print("")

# ### Test case #2 : test enroll_to_subject in case of invalid argument
# print("Test case #2 : test enroll_to_subject in case of invalid argument")
# print("Answer : Error")
# print(enroll_to_subject('66010001','CS101'))
# print("")

# ### Test case #3 : test enroll_to_subject in case of duplicate enrolled
# print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
# print("Answer : Already Enrolled")
# print(enroll_to_subject(student_list[0], subject_list[0]))
# print("")

# ### Test case #4 : test drop_from_subject in case of invalid argument 
# print("Test case #4 : test drop_from_subject in case of invalid argument")
# print("Answer : Error")
# print(drop_from_subject('66010001', 'CS101'))
# print("")

# ### Test case #5 : test drop_from_subject in case of not found 
# print("Test case #5 : test drop_from_subject in case of not found")
# print("Answer : Not Found")
# print(drop_from_subject(student_list[8], subject_list[0]))
# print("")

# ### Test case #6 : test drop_from_subject in case of drop successful
# print("Test case #6 : test drop_from_subject in case of drop successful")
# print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
# drop_from_subject(student_list[0], subject_list[0])
# print(list_student_enrolled_in_subject(subject_list[0].subject_id))
# print("")

# ### Test case #7 : test search_student_enrolled_in_subject
# print("Test case #7 : test search_student_enrolled_in_subject")
# print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
# lst = search_student_enroll_in_subject(subject_list[0])
# print([i.student.student_id for i in lst])
# print("")

# ### Test case #8 : get_no_of_student_enrolled
# print("Test case #8 get_no_of_student_enrolled")
# print("Answer : 5")
# print(get_no_of_student_enrolled(subject_list[0]))
# print("")

# ### Test case #9 : search_subject_that_student_enrolled
# print("Test case #9 search_subject_that_student_enrolled")
# print("Answer : ['CS102','CS103']")
# lst = search_subject_that_student_enrolled(student_list[0])
# print([i.subject.subject_id for i in lst])
# print("")

# ### Test case #10 : get_teacher_teach
# print("Test case #10 get_teacher_teach")
# print("Answer : Mr. Welsh")
# print(get_teacher_teach(subject_list[0]).teacher_name)
# print("")

# ### Test case #11 : search_enrollment_subject_student
# print("Test case #11 search_enrollment_subject_student")
# print("Answer : CS101 66010002")
# enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
# print(enroll.subject.subject_id,enroll.student.student_id)
# print("")

# ### Test case #12 : assign_grade
# print("Test case #12 assign_grade")
# print("Answer : Done")
# assign_grade(student_list[1],subject_list[0],'A')
# assign_grade(student_list[1],subject_list[1],'B')
# print(assign_grade(student_list[1],subject_list[2],'C'))
# print("")

# ### Test case #13 : get_student_record
# print("Test case #13 get_student_record")
# print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
# print(get_student_record(student_list[1]))
# print("")

# ### Test case #14 : get_student_GPS
# print("Test case #14 get_student_GPS")
# print("Answer : 3.0")
# print(get_student_GPS(student_list[1]))


class Enrollment:
    def __init__(self, student, subject, grade=None):
        self.student = student
        self.subject = subject
        self.grade = grade

def search_subject_by_id(subject_id):
    for subject in subject_list:
        if subject.get_subject_id() == subject_id:
            return subject
    return None

def search_student_by_id(student_id):
    for student in student_list:
        if student.get_student_id() == student_id:
            return student
    return None

def enroll_to_subject(student, subject):
    enrollment = search_enrollment_subject_student(subject, student)
    if enrollment is None:
        new_enrollment = Enrollment(student, subject)
        enrollment_list.append(new_enrollment)
        return "Done"
    else:
        return "Already Enrolled"

def drop_from_subject(student, subject):
    enrollment = search_enrollment_subject_student(subject, student)
    if enrollment is not None:
        enrollment_list.remove(enrollment)
        return "Done"
    else:
        return "Not Enrolled"

def search_enrollment_subject_student(subject, student):
    for enrollment in enrollment_list:
        if enrollment.subject == subject and enrollment.student == student:
            return enrollment
    return None

def search_student_enroll_in_subject(subject):
    return [enrollment for enrollment in enrollment_list if enrollment.subject == subject]

def search_subject_that_student_enrolled(student):
    return [enrollment for enrollment in enrollment_list if enrollment.student == student]

def assign_grade(student, subject, grade):
    enrollment = search_enrollment_subject_student(subject, student)
    if enrollment is not None:
        enrollment.grade = grade
        return "Done"
    else:
        return "Not Enrolled"

def get_teacher_teach(subject_search):
    for teacher in teacher_list:
        # Assuming a teacher can teach multiple subjects
        if subject_search in teacher.teaching_subjects:
            return teacher
    return None

def get_no_of_student_enrolled(subject):
    return len(search_student_enroll_in_subject(subject))

def get_student_record(student):
    record = {"Student ID": student.get_student_id(), "Student Name": student.get_student_name()}
    enrollments = search_subject_that_student_enrolled(student)
    record["Enrollments"] = [{"Subject ID": enrollment.subject.get_subject_id(),
                              "Subject Name": enrollment.subject.get_subject_name(),
                              "Grade": enrollment.grade} for enrollment in enrollments]
    return record

def get_student_GPS(student):
    total_credits = 0
    total_points = 0

    enrollments = search_subject_that_student_enrolled(student)
    for enrollment in enrollments:
        subject = enrollment.subject
        grade = enrollment.grade
        if grade:
            credit = subject.get_credit()
            total_credits += credit
            total_points += credit * grade_to_count(grade)

    if total_credits == 0:
        return 0.0
    else:
        return total_points / total_credits

# Assuming the teacher can teach multiple subjects
teacher1 = Teacher(teacher_id=1, teacher_name="Mr. Smith")
subject1 = Subject(subject_id=101, subject_name="Math", credit=3)
subject2 = Subject(subject_id=102, subject_name="English", credit=2)
teacher1.teaching_subjects = [subject1, subject2]

# Example usage:
# Create instances of Student, Teacher, and Subject
student1 = Student(student_id=1, student_name="John Doe")
subject1 = Subject(subject_id=101, subject_name="Math", credit=3)

# Enroll student in a subject
enroll_to_subject(student1, subject1)

# Drop student from a subject
drop_from_subject(student1, subject1)

# Assign a grade to a student in a subject
assign_grade(student1, subject1, 'A')

# Get teacher who teaches a specific subject
teacher = get_teacher_teach("Math")

# Get the number of students enrolled in a subject
num_students_enrolled = get_no_of_student_enrolled(subject1)

# Get the student's academic record
student_record = get_student_record(student1)

# Get the student's GPA
student_gpa = get_student_GPS(student1)

# List students enrolled in a subject
enrolled_students = list_student_enrolled_in_subject(subject1.get_subject_id())

# List subjects enrolled by a student
enrolled_subjects = list_subject_enrolled_by_student(student1.get_student_id())
