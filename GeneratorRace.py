import random

maxSkills = 0
maxSkills = int(input('Введите количество скиллов: '))
listSkills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']


class Race(object):

    def GeneratorSkills(self, maxSkills):
        z = 0
        while z < maxSkills:
            temp = random.randrange(0, 10)
            if temp == listSkills.index('speed'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                settingSkill : str = '"speed = "\n"', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '"'

            elif temp == listSkills.index('gravity'):
                valueOfSkill = random.randrange(60, 100)
                additionalValue = random.randrange(5, 8)
                settingSkill : str = '"gravity ="\n', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '"'

            elif temp == listSkills.index('hp'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                settingSkill = '"hp = "\n"', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'

            elif temp == listSkills.index('dmg'):
                valueOfSkill : float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill : str = '"dmg = "\n"', valueOfSkill, skillChange, ';', valueOfSkill+additionalValue, skillChange+additionalValueChange, ';', valueOfSkill+additionalValue*2, skillChange+additionalValueChange*2, ';', valueOfSkill+additionalValue*3, skillChange+additionalValueChange*3, '"'

            elif temp == listSkills.index('freeze'):
                valueOfSkill: float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill = '"freeze = "\n"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '"'

            elif temp == listSkills.index('burn'):
                valueOfSkill: float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill = '"burn = "\n"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '"'

            elif temp == listSkills.index('vampire'):
                valueOfSkill : float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                settingSkill : str = '"vampire = "\n"', valueOfSkill, skillChange, ';', valueOfSkill+additionalValue, skillChange+additionalValueChange, ';', valueOfSkill+additionalValue*2, skillChange+additionalValueChange*2, ';', valueOfSkill+additionalValue*3, skillChange+additionalValueChange*3, '"'

            elif temp == listSkills.index('longjump'):
                valueOfSkill = random.randrange(110, 600)
                additionalValue = random.randrange(10, 60)
                settingSkill = '"longjump ="\n', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'

            elif temp == listSkills.index('evasion'):
                valueOfSkill = random.randrange(0, 90)
                additionalValue = 0
                if valueOfSkill < 50:
                    additionalValue = random.randrange(3, 7)
                settingSkill = '"evasion"\n', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'

            elif temp == listSkills.index('step'):
                valueOfSkill: float = random.randrange(100, 200)
                additionalValue = random.randrange(5, 20)
                settingSkill = '"step"\n', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '"'

            elif temp == listSkills.index('paralyze'):
                valueOfSkill: float = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)

                settingSkill = '"paralyze = "\n"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '"'
            else:
                settingSkill = 'Error'
            z+=1
            return settingSkill
            print(settingSkill)
            obj.Output(settingSkill)
        print('Generate finish')

    def Output(self, settingSkill):
        print(settingSkill)

obj = Race()
obj.GeneratorSkills(maxSkills)
