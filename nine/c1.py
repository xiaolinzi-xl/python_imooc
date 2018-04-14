
class Student():
    # 一个班级里所有学生的总数
    sum = 0 # 类变量

    # 构造函数
    # 实例方法
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score = 0
        Student.sum += 1
        # print(age) 访问的是局部变量
        # print(name) 访问的是局部变量
        # print(Student.sum)
        # print(self.__class__.sum)
        print("当前班级的学生数为:" + str(Student.sum))

#   行为和特征
    def do_homework(self):
        print('homework')
    
    def mark(self,score):
        if score < 0:
            return '不能给别人打负分'
        else:
            self.__score = score
    
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
    
    @staticmethod
    def add(x,y):
        print()
    
    def do_english_homework(self):
        print('hello English')
    

# class Printer():
#     def print_file(self):
#         print("name: " + self.name)
#         print('age: ' + str(self.age))

# student = Student()
# student.print_file()

# student1 = Student()
# student2 = Student()
# student3 = Student()
# print(id(student1))
# print(id(student2))
# print(id(student3))

# student = Student('小林子',20)
# print(type(student))
# print(student.name)
# print(student.age)
# print(student.__dict__)
# print(Student.__dict__)

student1 = Student('小林子',23)
student1.mark(100)
student1.__score = -1
print(student1.__score)
# print(student1.__dict__)
# print(Student.sum)

# print(student1.__dict__)
# print(Student.__dict__)
# 公开的 public 私有的 private