import re

language = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}',language,re.I | re.S)
print(r)