
def print_student_files(name,gender='男',age=22,college='西电'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')
    print('我是' + gender + "生")
    print('我在' + college + '上学')

print_student_files('小林子','男',22,'西安电子科技大学')
print("---------------")
print_student_files('五天')
print('--------------')
print_student_files('小林',age=19,gender='女')
