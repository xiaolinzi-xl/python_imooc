import json

json_str = '[{"name":"qiyue","age":18,"flag":false},{"name":"qiyue","age":18}]'

student = json.loads(json_str)
print(type(student))
print(student)
# print(student['name'])
# print(student['age'])

# 反序列化 json串--->Python中的数据类型
# 序列化 Python中的数据类型--->json串