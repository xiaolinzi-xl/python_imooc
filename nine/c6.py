class People():
    sum = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        People.sum += 1
    
    def get_name(self):
        print(self.name)
    
    def do_homework(self,name):
        print('parent homework' + name)
