# 装饰器
# 特性 注解

import time

def f1():
    print('this is a function')

# unix 时间戳
# 对修改是封闭的，对扩展是开放的

def f2():
    print('this is a function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)