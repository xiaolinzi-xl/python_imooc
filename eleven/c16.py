origin = 0

def go(step):
    global origin # 扩大作用域
    new_pos = origin + step
    origin = new_pos
    return new_pos

print(go(2))
print(go(3))
print(go(6))