
def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1,damage2

damages = damage(3,6)
print(damages[0],damages[1])
print(type(damages)) # 元组 tuple

skill1_damage,skill2_damage = damage(3,6)
print(skill1_damage,skill2_damage)
