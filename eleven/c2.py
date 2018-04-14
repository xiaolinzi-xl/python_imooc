from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# print(type(VIP.BLACK))
# print(VIP.BLACK.name)
# print(VIP.BLACK.value)

# for x in VIP:
#     print(x)

# result = VIP.BLACK > VIP.GREEN 枚举不支持大小比较，支持等值比较
# print(result)

# result = VIP.GREEN == VIP1.GREEN
# print(result)
# print(type(VIP.BLACK))

a = 5
print(VIP(a))