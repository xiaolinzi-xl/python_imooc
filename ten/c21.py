import json

student = [
            {'name':'qiyue','age':18,'flag':False},
            {'name':'xiaoming','age':20}
        ]
json_str = json.dumps(student)
print(type(json_str))
print(json_str)