
# import sys
# sys.setrecursionlimit(1000) # 设置递归最大深度

def add(x,y):
    result = x + y
    return result

# def print(code): # 无限递归循环
#     print(code)

def print_code(code):
    print(code)

a = add(1,2)
b = print_code('python') 

print(a,b)