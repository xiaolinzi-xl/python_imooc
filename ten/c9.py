# 边界匹配
import re

qq = '101111110'

# r = re.findall('\d{4,8}',qq)
# ^开始字符 $末尾字符
r = re.findall('^\d{4,8}$',qq)
z = re.findall('^000',qq)
print(r,z)