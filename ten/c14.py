import re

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#',convert,language,1)
print(r)

