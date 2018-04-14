a = [1,2,3,4,5,6,7,8]

for i in range(0,len(a),2): # 打印 1,3,5,7
    print(a[i],end=' | ') 
print()
b = a[0:len(a):2] # 使用分片更加优雅
print(b)