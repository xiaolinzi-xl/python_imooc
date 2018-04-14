import re

a = 'C0C++9Java32C#11Python55Javascript'
r = re.findall('\D',a)
print(r)

# '\d' 0-9 数字字符 [0-9]'\D' 非数字字符 [^0-9]