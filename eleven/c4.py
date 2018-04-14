from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4

# 23种设计模式 单例模式