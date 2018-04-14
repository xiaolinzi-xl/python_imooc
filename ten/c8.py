# 数量词
import re

# a = 'python1111java678php'
# r = re.findall('[a-z]{3,6}?',a) # 贪婪匹配
# print(r)

# *匹配字符0次或无限多次
# +匹配字符1次或多次
# ?匹配0次或1次
# .匹配除换行符'\n'之外的所有字符
s = 'pytho0python1pythonn2'
r = re.findall('python?',s)
print(r)