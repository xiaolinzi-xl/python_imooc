# 列表推导式

a = [1,2,3,4,5,6,7,8]

b = [i*i for i in a]
c = [i*i for i in a if i > 5]
print(b)
print(c)