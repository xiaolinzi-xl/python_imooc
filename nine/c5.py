from c6 import People

# Student类继承People
class Student(People):
    def __init__(self,school,name,age):
        self.school = school
        # People.__init__(self,name,age)
        super(Student,self).__init__(name,age)
        Student.sum += 1
    
    def do_homework(self):
        print('do homework')

student1 = Student('农村小学',"石敢当",19)
print(student1.sum)
print(Student.sum)
print(student1.name)
print(student1.age)
People.do_homework("","xiaolinzi")
