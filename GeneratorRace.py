import random

maxSkills = 0
skillChange = 0
maxSkills = int(input('Введите количество скиллов: '))
required = int(input('Введите уровень: '))
listSkills = ['speed', 'gravity', 'hp', 'dmg', 'freeze', 'burn', 'vampire', 'longjump', 'evasion', 'step', 'paralyze']
tempList = []


class Race(object):

    def DefaultForm(self, tempList):
        print('\t\"name\"\n\t{\n\t\t\"name\"            \"name\"\n\t\t\"required\"        \"' + str(required) +  '\"\n\t\t\"author\"          \"Magnus\"\n\t\t\"category\"        \"Девятый дивизион(30000-45000)\"\n\t\t\"maxlvl\"          \"1000\"\n\t\t\"teamlimit\"       \"0\"\n\t\t\"skillamount\"     \"' + str(maxSkills) + '\"\n\t\t\"skilllvls\"       \"0\"\n\t\t\"skillsets\"       \"4\"\n\t\t\"skillnames\"      \"none\"\n\t\t\"skilldesc\"       \"none\"')


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
                valueOfSkill/=100
                additionalValue = random.randrange(10, 40)
                additionalValue/=100
                round(additionalValue, 3)
                round(valueOfSkill, 3)
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"speed =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill) + ';' + str(float(valueOfSkill+additionalValue)) + ';' + str(float(valueOfSkill+additionalValue))*2 + ';' + str(float(valueOfSkill+additionalValue))*3 + '\"')
            elif temp == listSkills.index('gravity'):
                valueOfSkill = random.randrange(60, 100)
                additionalValue = random.randrange(5, 8)
                additionalValue /= 100
                valueOfSkill /= 100
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"gravity =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill) + ';' + str(round(float(valueOfSkill-additionalValue), 3)) + ';' + str(round(float(valueOfSkill-additionalValue*2), 3)) + ';' + str(round(float(valueOfSkill-additionalValue*3), 3)) + '\"')

            elif temp == listSkills.index('hp'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"hp =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(int(valueOfSkill + additionalValue * 2)) + ';' + str(int(valueOfSkill + additionalValue * 3)) + '\"')

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
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"dmg =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill), str(skillChange) + ';' + str(int(valueOfSkill+additionalValue)), str(int(skillChange+additionalValueChange)) + ';' + str(round(valueOfSkill+additionalValue*2, 3)), str(int(skillChange+additionalValueChange*2)) + ';' + str(round(valueOfSkill+additionalValue*3, 3)), str(int(skillChange+additionalValueChange*3)) + '\"')

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
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"freeze =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill), str(skillChange) + ';' + str(round(valueOfSkill + additionalValue, 3)), str(int(skillChange + additionalValueChange)) + ';' + str(round(valueOfSkill + additionalValue * 2, 3)), str(int(skillChange + additionalValueChange * 2)) + ';' + str(round(valueOfSkill + additionalValue * 3, 3)), str(int(skillChange + additionalValueChange * 3)) + '\"')

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
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"burn =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill), str(skillChange) + ';' + str(round(float(valueOfSkill + additionalValue), 3)) + ' ' + str(int(skillChange + additionalValueChange)) + ';' + str(round(float(valueOfSkill + additionalValue * 2), 3)), str(int(skillChange + additionalValueChange * 2)) + ';' + str(round(float(valueOfSkill + additionalValue * 3), 3)), str(int(skillChange + additionalValueChange * 3)) + '\"')

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
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"vampire =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill), str(skillChange) + ';' + str(round(valueOfSkill+additionalValue, 3)), str(int(skillChange+additionalValueChange)) + ';' + str(round(valueOfSkill+additionalValue*2, 3)), str(int(skillChange+additionalValueChange*2)) + ';' + str(round(valueOfSkill+additionalValue*3, 3)), str(int(skillChange+additionalValueChange*3)) + '\"')

            elif temp == listSkills.index('longjump'):
                valueOfSkill = random.randrange(110, 600)
                additionalValue = random.randrange(10, 60)
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"longjump =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(int(valueOfSkill + additionalValue * 2)) + ';' + str(int(valueOfSkill + additionalValue * 3)) + '\"')

            elif temp == listSkills.index('evasion'):
                valueOfSkill = random.randrange(0, 60)
                additionalValue = 0
                if valueOfSkill < 50:
                    additionalValue = random.randrange(3, 7)
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"evasion\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(int(valueOfSkill + additionalValue * 2)) + ';' + str(int(valueOfSkill + additionalValue * 3)) + '\"')

            elif temp == listSkills.index('step'):
                valueOfSkill = random.randrange(100, 200)
                additionalValue = random.randrange(5, 20)
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"step\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(int(valueOfSkill + additionalValue * 2)) + ';' + str(int(valueOfSkill + additionalValue * 3)) + '\"')

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
                print('\t\t\"skill' + str(int(z+1)) + '\"          \"paralyze =\"\n\t\t\"setting' + str(int(z+1)) + '\"', '       \"' + str(valueOfSkill), str(skillChange) + ';' + str(int(valueOfSkill + additionalValue)),  str(int(skillChange + additionalValueChange)) + ';' + str(round(valueOfSkill + additionalValue * 2, 3)), str(int(skillChange + additionalValueChange * 2)) + ';' + str(round(valueOfSkill + additionalValue * 3, 3)), str(int(skillChange + additionalValueChange * 3)) + '\"')
            else:
                settingSkill = 'Error'
            #obj.Output(0, settingSkill, temp, valueOfSkill, skillChange, additionalValue, additionalValueChange)
            z+=1
        print('\t}')
        print('Generate is over')


    def Output(self, settingSkill):
        print(settingSkill)

obj = Race
obj.DefaultForm(0, tempList)
obj.GeneratorSkills(0, maxSkills)
input()

