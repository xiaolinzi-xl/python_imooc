import re

a = 'C|C++|Java|C#|Python|Javascript'

r = re.findall('Python',a)
if len(r) != 0:
    print('字符串中包含Python')
else:
    print('No')
print(r)

# print(a.index('Python') > -1)
# print('Python' in a)
