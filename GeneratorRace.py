import random

maxSkills = 0
int(input('Введите название скиллов (speed, gravity, hp, dmg, freeze, burn, vampire, longjump, evasion, step, paralyze)', maxSkills))
listSkills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']

def GeneratorSkills(maxSkills):
    z = 0
    while z <= maxSkills:
        temp = random.randrange(0, 10)
        if temp == listSkills.index('speed') or temp == listSkills.index()