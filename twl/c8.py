import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print('this is a function' + func_name)

@decorator
def f2(func_name1,func_name2):
    print('haha ' + func_name1 + ' ' + func_name2)

@decorator
def f3(func_name1,func_name2,**kw):
    print('haha ' + func_name1 + ' ' + func_name2)
    print(kw)
    # print(type(kw))


# f = decorator(f1)
# f()
# @ 设计模式中的动态代理 异曲同工之妙 AOP编程思想
# Python支持函数嵌套
# *args 可变参数 元组 tuple
# **kw 关键字参数 字典 dict
f1('xiaolinzi')
f2('haha','shazi')

f3('haha','xiaolinzi',a=1,b=2,c=3)