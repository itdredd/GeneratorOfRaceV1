import random

maxSkills = 0
int(input('Введите название скиллов (speed, gravity, hp, dmg, freeze, burn, vampire, longjump, evasion, step, paralyze)', maxSkills))
listSkills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']

def GeneratorSkills(maxSkills):
    z = 0
    while z <= maxSkills:
        temp = random.randrange(0, 10)
        if temp == listSkills.index('speed'):
            valueOfSkill = random.randrange(100, 150)
            additionalValue = random.randrange(10, 40)
            settingsSkill : str = '"soeed = "\n"', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '"'
        if temp == listSkills.index('gravity')
            valueOfSkill = random.randrange(60, 100)
            additionalValue = random.randrange(5, 8)
            settingsSkill : str = '"gravity ="\n', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '"'
        if temp == listSkills.index('hp'):
            valueOfSkill = random.randrange(100, 150)
            additionalValue = random.randrange(10, 40)
            settingsSkill: str = '"hp = "\n"', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'
        if temp == listSkills.index(dmg):
            valueOfSkill : float = random.randrange(100, 150)
            valueOfSkill /= 100









