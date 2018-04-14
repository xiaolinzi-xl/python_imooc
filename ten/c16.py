import re

s = '78C7321D86'

r = re.match('\d',s) # 从首字母开始匹配,一旦发现匹配立刻停止搜索

r1 = re.search('\d',s) # 一旦发现匹配立刻停止搜索

r2 = re.findall('\d',s)
print(r.group())
print(r1.group())
print(r2)