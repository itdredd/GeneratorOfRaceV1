import random

level = input('Write required lvl: ')
author = 'Magnus'
category: str = 'Девятый дивизион(30000-45000)'
skills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']
#print(enumerate(skills, start=1))
rand = random.randrange(0, 11)
if rand == skills.index('speed'):
    print('Founded')
else:
    print(rand)
    print('No found')