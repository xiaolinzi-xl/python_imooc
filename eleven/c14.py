
def f1():
    a = 10
    def f2():
        # a此时被Python认为是局部变量
        # a = 20
        # print(a)
        return a
    return f2

f = f1()
print(f)
print(f.__closure__)