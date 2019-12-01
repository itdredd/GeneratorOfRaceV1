import random

maxSkills = 0
skillChange = 0
maxSkills = int(input('Введите количество скиллов: '))
required = int(input('Введите уровень: '))
listSkills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']
tempList = []


class Race(object):

    def DefaultForm(self, tempList):
        print('\"name\"\n{\n\"name\" \"name\"\n\"required\" \"', required,  '\"\n\"author\" \"Magnus\"\n\"category\" \"Девятый дивизион(30000-45000)\"\n\"maxlvl\" \"1000\"\n\"teamlimit\" \"0\"\n\"skillamount\" \"', maxSkills, '\"\n\"skilllvls\" \"0\"\n\"skillsets\" \"4\"\n\"skillnames\" \"none\"\n\"skilldesc\" \"none\"')


    def GeneratorSkills(self, maxSkills):
        z = 0
        while z < maxSkills:
            temp = random.randrange(0, 10)
            if z != 0:
                while temp in tempList:
                    temp = random.randrange(0, 11)
            tempList.append(temp)
            if temp == listSkills.index('speed'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                print('\"skill' + str(int(z+1)), '\" \"speed =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, ';', valueOfSkill+additionalValue, ';', valueOfSkill+additionalValue*2, ';', valueOfSkill+additionalValue*3, '\"')
            elif temp == listSkills.index('gravity'):
                valueOfSkill = random.randrange(60, 100)
                additionalValue = random.randrange(5, 8)
                additionalValue /= 100
                valueOfSkill /= 100
                print('\"skill' + str(int(z+1)), '\" \"gravity =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, ';', valueOfSkill-additionalValue, ';', valueOfSkill-additionalValue*2, ';', valueOfSkill-additionalValue*3, '\"')

            elif temp == listSkills.index('hp'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                print('\"skill' + str(int(z+1)), '\" \"hp =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '\"')

            elif temp == listSkills.index('dmg'):
                valueOfSkill = random.randrange(100, 150)
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
                print('\"skill' + str(int(z+1)), '\" \"dmg =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, skillChange, ';', valueOfSkill+additionalValue, skillChange+additionalValueChange, ';', round(valueOfSkill+additionalValue*2, 3), skillChange+additionalValueChange*2, ';', round(valueOfSkill+additionalValue*3, 3), skillChange+additionalValueChange*3, '\"')

            elif temp == listSkills.index('freeze'):
                valueOfSkill= random.randrange(100, 150)
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
                print('\"skill' + str(int(z+1)), '\" \"freeze =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, skillChange, ';', round(valueOfSkill + additionalValue, 3), skillChange + additionalValueChange, ';', round(valueOfSkill + additionalValue * 2, 3), skillChange + additionalValueChange * 2, ';', round(valueOfSkill + additionalValue * 3, 3), skillChange + additionalValueChange * 3, '\"')

            elif temp == listSkills.index('burn'):
                valueOfSkill= random.randrange(100, 150)
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
                print('\"skill' + str(int(z+1)), '\" \"burn =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', valueOfSkill + additionalValue * 2, skillChange + additionalValueChange * 2, ';', valueOfSkill + additionalValue * 3, skillChange + additionalValueChange * 3, '\"')

            elif temp == listSkills.index('vampire'):
                valueOfSkill= random.randrange(100, 150)
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
                print('\"skill' + str(int(z+1)), '\" \"vampire =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, skillChange, ';', round(valueOfSkill+additionalValue, 3), skillChange+additionalValueChange, ';', round(valueOfSkill+additionalValue*2, 3), skillChange+additionalValueChange*2, ';', round(valueOfSkill+additionalValue*3, 3), skillChange+additionalValueChange*3, '\"')

            elif temp == listSkills.index('longjump'):
                valueOfSkill = random.randrange(110, 600)
                additionalValue = random.randrange(10, 60)
                print('\"skill' + str(int(z+1)), '\" \"longjump =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '\"')

            elif temp == listSkills.index('evasion'):
                valueOfSkill = random.randrange(0, 90)
                additionalValue = 0
                if valueOfSkill < 50:
                    additionalValue = random.randrange(3, 7)
                print('\"skill' + str(int(z+1)), '\" \"evasion\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '\"')

            elif temp == listSkills.index('step'):
                valueOfSkill = random.randrange(100, 200)
                additionalValue = random.randrange(5, 20)
                print('\"skill' + str(int(z+1)), '\" \"step\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, ';', valueOfSkill + additionalValue, ';', valueOfSkill + additionalValue * 2, ';', valueOfSkill + additionalValue * 3, '\"')

            elif temp == listSkills.index('paralyze'):
                valueOfSkill = random.randrange(100, 150)
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
                print('\"skill' + str(int(z+1)), '\" \"paralyze =\"\n\"setting' + str(int(z+1)), '\"', valueOfSkill, skillChange, ';', valueOfSkill + additionalValue, skillChange + additionalValueChange, ';', round(valueOfSkill + additionalValue * 2, 3), skillChange + additionalValueChange * 2, ';', round(valueOfSkill + additionalValue * 3, 3), skillChange + additionalValueChange * 3, '\"')
            else:
                settingSkill = 'Error'
            #obj.Output(0, settingSkill, temp, valueOfSkill, skillChange, additionalValue, additionalValueChange)
            z+=1
        print('}')
        print('Generate is over')


    def Output(self, settingSkill):
        print(settingSkill)

obj = Race
obj.DefaultForm(0, tempList)
obj.GeneratorSkills(0, maxSkills)
input()

