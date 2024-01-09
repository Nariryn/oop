class student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
stu1 = student('001', "John")
stu2 = student('002', "Peter")
print(stu1.id)
print(stu2.id)

'''
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Subject :
    def __init__(self, sub_id, sub_name):
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.student_list = []
        
stu1 = Student('001', 'John')
stu2 = Student('002', 'Peter')
sub1 = Subject('01076140', 'Calculus')

sub1.student_list.append(stu1)
sub1.student_list.append(stu2)
print(sub1.student_list)
'''