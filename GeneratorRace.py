import random

maxSkills = 0
int(input('Введите название скиллов (speed, gravity, hp, dmg, freeze, burn, vampire, longjump, evasion, step, paralyze)', maxSkills))
listSkills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']

class Race(object):
    def GeneratorSkills(self, maxSkills):
        z = 0
        while z <= maxSkills:
            temp = random.randrange(0, 10)
            if temp == listSkills.index('speed'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                settingsSkill : str = '"soeed = "\n"', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '"'
                return settingsSkill

            if temp == listSkills.index('gravity')
                valueOfSkill = random.randrange(60, 100)
                additionalValue = random.randrange(5, 8)
                settingsSkill : str = '"gravity ="\n', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '"'
                return settingsSkill

            if temp == listSkills.index('hp'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                settingsSkill: str = '"hp = "\n"', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'
                return settingsSkill

            if temp == listSkills.index('dmg'):
                valueOfSkill : float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                if skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                if skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill : str = '"dmg = "\n"', valueOfSkill, skillChange, ';', valueOfSkill+additionalValue, skillChange+additionalValueChange, ';', valueOfSkill+additionalValue*2, skillChange+additionalValueChange*2, ';', valueOfSkill+additionalValue*3, skillChange+additionalValueChange*3, '"'
                return settingSkill

            if temp == listSkills.index('freeze'):
                valueOfSkill: float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                if skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                if skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill: str = '"freeze = "\n"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '"'
                return settingSkill

            if temp == listSkills.index('burn'):
                valueOfSkill: float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                if skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                if skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill: str = '"burn = "\n"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '"'
                return settingSkill

            if temp == listSkills.index('vampire'):
                valueOfSkill : float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                if skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                if skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill : str = '"vampire = "\n"', valueOfSkill, skillChange, ';', valueOfSkill+additionalValue, skillChange+additionalValueChange, ';', valueOfSkill+additionalValue*2, skillChange+additionalValueChange*2, ';', valueOfSkill+additionalValue*3, skillChange+additionalValueChange*3, '"'
                return settingSkill

            if temp == listSkills.index('longjump'):
                valueOfSkill = random.randrange(110, 600)
                additionalValue = random.randrange(10, 60)
                settingsSkill: str = '"longjump ="\n', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'
                return settingsSkill

            if temp == listSkills.index('evastion'):
                valueOfSkill = random.randrange(0, 90)
                if valueOfSkill < 50:
                    additionalValue = random.randrange(3, 7)
                settingsSkill: str = '"evastion"\n', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'
                return settingsSkill

            if temp == listSkills.index('step'):
                valueOfSkill: float = random.randrange(100, 200)
                additionalValue = random.randrange(5, 20)
                settingsSkill: str = '"step"\n', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'
                return settingsSkill

            if temp == listSkills.index('paralyze'):
                valueOfSkill: float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                if skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                if skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill: str = '"paralyze = "\n"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '"'
                return settingSkill
