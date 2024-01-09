class Student:
    def __init__(self, student_id, student_name, menter=None):
        self.student_id = student_id
        self.student_name = student_name
        self.menter = menter
    def add_metor(self,pe):
        self.menter = pe

student_a = Student("66010405", "Alice")
student_b = Student("66010261", "Nut")
student_c = Student("65010731", "Mew")
student_d = Student("64010123", "Kid")
student_e = Student("63010432", "Sand")

student_a.add_metor(student_c)
student_c.add_metor(student_d)
student_d.add_metor(student_e)

students = [student_a, student_b, student_c, student_d, student_e]

def who_chain_mentor(student_id):
    id_chain = []
    current_student = None
    for student in students :
        if student.student_id == student_id :
            current_student = student.menter
    while current_student != None :
        id_chain.append(current_student.student_id)
        if current_student.menter == None:
            break
        current_student = current_student.menter
    return id_chain

print(who_chain_mentor('66010405'))

def is_mentor(x, y):
    chain_x = who_chain_mentor(x)
    return y in chain_x

print(is_mentor('66010405', '65010731'))