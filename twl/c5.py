
list_x = [1,0,1,0,0,1]
list_u = ['a','B','c','F','e']
# filter函数返回结果代表真/假，True/False
r = filter(lambda x:True if x==1 else False,list_x)
r1 = filter(lambda x:x >= 'A' and x <= 'Z',list_u)
print(list(r))
print(list(r1))