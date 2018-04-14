import re

s = 'life is short,i use python,i love python'

r = re.search('life(.*)python(.*)python',s)
r1 = re.findall('life(.*)python',s)
print(r.groups())
print(r1)