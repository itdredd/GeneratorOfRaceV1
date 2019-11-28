import random
from GeneratorRaceOutput import Output

Output()
level = input('Write required lvl: ')
amountSkills = int(input('Write amount of skills: '))
author = 'Magnus'
category: str = 'Девятый дивизион(30000-45000)'
skills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']
# print(enumerate(skills, start=1))
z = 0
rand = 0
buffer = 0
while z < amountSkills:
    rand = random.randrange(0, 10)
    while buffer == rand:
        rand = random.randrange(0, 10)
    if rand == skills.index('speed'):
        # print('Found:', rand)
        speedValue = random.randrange(100, 150)
        speedValue = speedValue // 10 * 10
        additionalValue = random.randrange(10, 40)
        additionalValue = additionalValue // 10 * 10
        print('"speed ="\n"', speedValue, ';', speedValue + additionalValue, ";", speedValue + additionalValue * 2, ";",
              speedValue + additionalValue * 3, '"')
    if rand == skills.index('gravity'):
        # print('\nFound:', rand)
        gravityValue = float(random.randrange(60, 100))
        gravityValue /= 100
        gravityValue = round(gravityValue, 1)
        # speedValue //= 10
        additionalValue = random.randrange(5, 8)
        additionalValue /= 100
        print('"gravity = "\n"', gravityValue, ';', round(gravityValue - additionalValue, 2), ':',
              round(gravityValue - additionalValue * 2, 2), ':', round(gravityValue - additionalValue * 3, 2), '"')
    if rand == skills.index('hp'):
        startHpValue = random.randrange(90, 180)
        additionalValue = random.randrange(10, 30)
        print('"hp = "\n"', startHpValue, ';', startHpValue + additionalValue, ';', startHpValue + additionalValue * 2,
              ';', startHpValue + additionalValue * 3, '"')
    if rand == skills.index('dmg'):
        startDmgValue: float = random.randrange(100, 150)
        startDmgValue /= 100
        additionalValue = random.randrange(100, 500)
        additionalValue /= 1000
        dmgChange = random.randrange(0, 90)
        additionalValueChange = 0
        if 30 < dmgChange < 50:
            additionalValueChange = random.randrange(0, 10)
        if dmgChange < 30:
            additionalValueChange = random.randrange(10, 15)
        print('"dmg ="\n"', startDmgValue, dmgChange, ';', round(startDmgValue + additionalValue, 2),
              dmgChange + additionalValueChange, ';', round(startDmgValue + additionalValue * 2, 2),
              dmgChange + additionalValueChange * 2, ';', round(startDmgValue + additionalValue * 3, 2),
              dmgChange + additionalValueChange * 3, ';')
    if rand == skills.index('freeze'):
        startFreezeValue = random.randrange(500, 1500);
        startFreezeValue = startFreezeValue / 1000
        startFreezeValue = round(startFreezeValue, 2)
        additionalValue = random.randrange(500, 4000)
        additionalValue /= 10000
        round(additionalValue, 2)
        freezeChange = random.randrange(0, 90)
        additionalValueChange = 0
        if 30 < freezeChange < 50:
            additionalValueChange = random.randrange(0, 10)
        if freezeChange < 30:
            additionalValueChange = random.randrange(10, 15)
        print('"freeze = "\n"', startFreezeValue, freezeChange, ';', round(startFreezeValue + additionalValue, 2),
              round(freezeChange + additionalValueChange, 2), ';', round(startFreezeValue + additionalValue * 2, 2),
              round(freezeChange + additionalValueChange * 2, 2), ';', round(startFreezeValue + additionalValue * 3, 2),
              round(freezeChange + additionalValueChange * 3, 2), '"')
    if rand == skills.index('burn'):
        burnValue = random.randrange(500, 1500)
        burnValue = burnValue / 1000
        burnValue = round(burnValue, 2)
        additionalValue = random.randrange(500, 4000)
        additionalValue /= 10000
        round(additionalValue, 2)
        burnChange = random.randrange(0, 90)
        additionalValueChange = 0
        if 30 < burnChange < 50:
            additionalValueChange = random.randrange(0, 10)
        if burnChange < 30:
            additionalValueChange = random.randrange(10, 15)
        print('"burn = "\n"', burnValue, burnChange, ';', round(burnValue + additionalValue, 2),
              round(burnChange + additionalValueChange, 2), ';', round(burnValue + additionalValue * 2, 2),
              round(burnChange + additionalValueChange * 2, 2), ';', round(burnValue + additionalValue * 3, 2),
              round(burnChange + additionalValueChange * 3, 2), '"')
    if rand == skills.index('vampire'):
        vampireValue: float = random.randrange(100, 150)
        vampireValue /= 100
        additionalValue = random.randrange(100, 500)
        additionalValue /= 1000
        vampireChange = random.randrange(0, 90)
        additionalValueChange = 0
        if 30 < vampireChange < 50:
            additionalValueChange = random.randrange(0, 10)
        if vampireChange < 30:
            additionalValueChange = random.randrange(10, 15)
        print('"vampire ="\n"', vampireValue, vampireChange, ';', round(vampireValue + additionalValue, 2),
              vampireChange + additionalValueChange, ';', round(vampireValue + additionalValue * 2, 2),
              vampireChange + additionalValueChange * 2, ';', round(vampireValue + additionalValue * 3, 2),
              vampireChange + additionalValueChange * 3, ';')
    if rand == skills.index('longjump'):
        longjumpValue = random.randrange(110, 1000)
        longjumpValue = longjumpValue // 10 * 10
        if longjumpValue < 600:
            additionalValue = random.randrange(50, 100)
        else:
            additionalValue = 0
        print('"longjump ="\n"', longjumpValue, ';', longjumpValue + additionalValue, ';',
              longjumpValue + additionalValue * 2, ';', longjumpValue + additionalValue * 3, '"')
    if rand == skills.index('evasion'):
        evasionValue = random.randrange(0, 90)
        if 60 < evasionValue < 90:
            additionalValue = 0
        if 30 < evasionValue < 60:
            additionalValue = random.randrange(0, 5)
        if evasionValue < 30:
            additionalValue = random.randrange(5, 8)
        print('"evasion"\n"', evasionValue, ';', evasionValue + additionalValue, ';',
              evasionValue + additionalValue * 2, ';', evasionValue + additionalValue * 3, '"')
    if rand == skills.index('step'):
        stepValue: float = random.randrange(100, 200)
        additionalValue = random.randrange(5, 20)
        print('"step"\n"', stepValue, ';', stepValue + additionalValue, ';', stepValue + additionalValue * 2, ';',
              stepValue + additionalValue * 3, '"')
    if rand == skills.index('paralyze'):
        paralyzeValue: float = random.randrange(100, 150)
        paralyzeValue /= 100
        additionalValue = random.randrange(100, 500)
        additionalValue /= 1000
        paralyzeChange = random.randrange(0, 90)
        additionalValueChange = 0
        if 30 < paralyzeChange < 50:
            additionalValueChange = random.randrange(0, 10)
        if paralyzeChange < 30:
            additionalValueChange = random.randrange(10, 15)
        paralyzeSetting = '"paralyze ="\n"', paralyzeValue, paralyzeChange, ';', round(paralyzeValue + additionalValue, 2), paralyzeChange + additionalValueChange, ';', round(paralyzeValue + additionalValue * 2, 2), paralyzeChange + additionalValueChange * 2, ';', round(paralyzeValue + additionalValue * 3, 2), paralyzeChange + additionalValueChange * 3, ';'
    # else:
    #     print(rand)
    #     print("Need add soon...")

    z+=1
