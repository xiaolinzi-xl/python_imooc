import re

s = 'A8C7321D86'

def convert(value):
    matched = value.group() # 拿到具体的变量
    if int(matched) > 6:
        return '9'
    else:
        return '6'

r = re.sub('\d',convert,s)
print(r)