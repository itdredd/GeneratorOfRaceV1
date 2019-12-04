import random


class Race(object):
    tempList = []
    required = 0
    name: str = 0
    author = "Dredd"
    category = 0
    maxLvl = 1000
    teamLimit = 0
    skillAmount = 0
    skillLvls = "0"
    skillSets = 0
    skillNames = 0
    skillDesc = 0
    listSkills = ['speed', 'gravity', 'hp', 'invis', 'dmg', 'freeze', 'burn', 'vampire', 'boom', 'regen', 'slow',
                  'rockets', 'longjump', 'mirror', 'evasion', 'step', 'push', 'respawn', 'dropweapon', 'paralyze',
                  'blind', 'poison', 'illusion', 'bury']
    listUltimate = ['teleport', 'jetpack', 'explode', 'ultfreeze', 'CreateProp', 'ultgod', 'webshot', 'ultburn',
                    'speedbuf', 'heal', 'ultblind','ultremove', 'ultburyme', 'fatality', 'blink', 'ultswap', 'sphere',
                    'chaos', 'teleportator', 'portals']

    def Input(self):
        self.required, self.name, self.skillAmount = map(str,
                                                         input("Введите уровень, название и кол-во скиллов: ").split())

    def GenerateSkills(self):
        z = 0
        temp = 0
        tempprev = 0
        while z < int(self.skillAmount):
            temp = random.randrange(0, 24)
            while temp in self.tempList:
                temp = random.randrange(0, 24)
            if temp == self.listSkills.index('speed'):
                print('Скорость', end=''),
            if temp == self.listSkills.index('gravity'):
                print('Гравитация', end=''),
            if temp == self.listSkills.index('hp'):
                print('Здоровье', end=''),
            if temp == self.listSkills.index('invis'):
                print('Невидимость', end=''),
            if temp == self.listSkills.index('dmg'):
                print('Урон', end=''),
            if temp == self.listSkills.index('freeze'):
                print('Заморозка', end=''),
            if temp == self.listSkills.index('burn'):
                print('Поджег', end=''),
            if temp == self.listSkills.index('vampire'):
                print('Вампирка', end=''),
            if temp == self.listSkills.index('boom'):
                print('Взрыв', end=''),
            if temp == self.listSkills.index('regen'):
                print('Регенирация', end=''),
            if temp == self.listSkills.index('slow'):
                print('Замедление', end=''),
            if temp == self.listSkills.index('rockets'):
                print('Ракеты', end=''),
            if temp == self.listSkills.index('longjump'):
                print('Длинный прыжок', end=''),
            if temp == self.listSkills.index('mirror'):
                print('Зеркало', end=''),
            if temp == self.listSkills.index('evasion'):
                print('Уклон', end=''),
            if temp == self.listSkills.index('step'):
                print('Высота шага', end=''),
            if temp == self.listSkills.index('push'):
                print('Отброс', end=''),
            if temp == self.listSkills.index('respawn'):
                print('Возрождение', end=''),
            if temp == self.listSkills.index('dropweapon'):
                print('Выброс оружия', end=''),
            if temp == self.listSkills.index('paralyze'):
                print('Паралич', end=''),
            if temp == self.listSkills.index('blind'):
                print('Ослепление', end=''),
            if temp == self.listSkills.index('poison'):
                print('Яд', end=''),
            if temp == self.listSkills.index('illusion'):
                print('Иллюзия', end=''),
            if temp == self.listSkills.index('bury'):
                print('Подкоп', end=''),
            if z + 1 != int(self.skillAmount):
                print(';', end=''),
            if temp != tempprev:
                self.tempList.append(temp)
            tempprev = temp
            z += 1

        print('\"\n\t\"skilldesc\"\t\"', end='')
        z = 0
        while z < int(self.skillAmount):
            if self.tempList[z] == self.listSkills.index('speed'):
                print('speed', end=''),
            if self.tempList[z] == self.listSkills.index('gravity'):
                print('gravity', end=''),
            if self.tempList[z] == self.listSkills.index('hp'):
                print('hp', end=''),
            if self.tempList[z] == self.listSkills.index('invis'):
                print('invis', end=''),
            if self.tempList[z] == self.listSkills.index('dmg'):
                print('dmg', end=''),
            if self.tempList[z] == self.listSkills.index('freeze'):
                print('freeze', end=''),
            if self.tempList[z] == self.listSkills.index('burn'):
                print('burn', end=''),
            if self.tempList[z] == self.listSkills.index('vampire'):
                print('vampire', end=''),
            if self.tempList[z] == self.listSkills.index('boom'):
                print('boom', end=''),
            if self.tempList[z] == self.listSkills.index('regen'):
                print('regen', end=''),
            if self.tempList[z] == self.listSkills.index('slow'):
                print('slow', end=''),
            if self.tempList[z] == self.listSkills.index('rockets'):
                print('rockets', end=''),
            if self.tempList[z] == self.listSkills.index('longjump'):
                print('longjump', end=''),
            if self.tempList[z] == self.listSkills.index('mirror'):
                print('mirror', end=''),
            if self.tempList[z] == self.listSkills.index('evasion'):
                print('evasion', end=''),
            if self.tempList[z] == self.listSkills.index('step'):
                print('step', end=''),
            if self.tempList[z] == self.listSkills.index('push'):
                print('push', end=''),
            if self.tempList[z] == self.listSkills.index('respawn'):
                print('respawn', end=''),
            if self.tempList[z] == self.listSkills.index('dropweapon'):
                print('dropweapon', end=''),
            if self.tempList[z] == self.listSkills.index('paralyze'):
                print('paralyze', end=''),
            if self.tempList[z] == self.listSkills.index('blind'):
                print('blind', end=''),
            if self.tempList[z] == self.listSkills.index('poison'):
                print('poison', end=''),
            if self.tempList[z] == self.listSkills.index('illusion'):
                print('illusion', end=''),
            if self.tempList[z] == self.listSkills.index('bury'):
                print('bury', end=''),

            if z + 1 != int(self.skillAmount):
                print(';', end=''),
            if temp != tempprev:
                self.tempList.append(temp)
            tempprev = temp
            z += 1
        print('\"', end=''),

    def DefaultForm(self):
        print('\"' + self.name + '\"\n{\n\t\"name\"\t\"' + self.name + '\"\n\t\"required\"\t\"' + str(
            self.required) + '\"\n\t\"category\"\t\"Девятый дивизион('
                             '30000-45000)\"\n\t\"maxlvl\"\t\"1000\"\n\t\"teamlimit\"\t\"1000\"\n\t\"skillamount\"\t'
                             '\"' + str(
            self.skillAmount) + '\"\n\t\"skilllvls\"\t\"0\"\n\t\"skillsets\"\t\"4\"\n\t\"skillnames\"\t\"', end=''),

    def GenerateParams(self):
        i = 0
        while i < int(self.skillAmount):
            if self.tempList[i] == self.listSkills.index('speed'):
                valueOfSkill = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(10, 40)
                additionalValue /= 100
                round(additionalValue, 3)
                round(valueOfSkill, 3)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"speed =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(round(valueOfSkill, 3)) + ';' + str(
                          round(float(valueOfSkill + additionalValue), 3)) + ';' + str(
                          round(float(valueOfSkill + additionalValue * 2), 3)) + ';' + str(
                          round(float(valueOfSkill + additionalValue * 3), 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('gravity'):
                valueOfSkill = random.randrange(60, 100)
                additionalValue = random.randrange(5, 8)
                additionalValue /= 100
                valueOfSkill /= 100
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"gravity =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill) + ';' + str(
                          round(float(valueOfSkill - additionalValue), 3)) + ';' + str(
                          round(float(valueOfSkill - additionalValue * 2), 3)) + ';' + str(
                          round(float(valueOfSkill - additionalValue * 3), 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('hp'):
                valueOfSkill = random.randrange(100, 150)
                additionalValue = random.randrange(10, 40)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"hp =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(
                          int(valueOfSkill + additionalValue * 2)) + ';' + str(
                          int(valueOfSkill + additionalValue * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('dmg'):
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
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"dmg =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill),
                      str(skillChange) + ';' + str(int(valueOfSkill + additionalValue)),
                      str(int(skillChange + additionalValueChange)) + ';' + str(
                          round(valueOfSkill + additionalValue * 2, 3)),
                      str(int(skillChange + additionalValueChange * 2)) + ';' + str(
                          round(valueOfSkill + additionalValue * 3, 3)),
                      str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('freeze'):
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
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"freeze =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill),
                      str(skillChange) + ';' + str(round(valueOfSkill + additionalValue, 3)),
                      str(int(skillChange + additionalValueChange)) + ';' + str(
                          round(valueOfSkill + additionalValue * 2, 3)),
                      str(int(skillChange + additionalValueChange * 2)) + ';' + str(
                          round(valueOfSkill + additionalValue * 3, 3)),
                      str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('burn'):
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
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"burn =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill),
                      str(skillChange) + ';' + str(round(float(valueOfSkill + additionalValue), 3)) + ' ' + str(
                          int(skillChange + additionalValueChange)) + ';' + str(
                          round(float(valueOfSkill + additionalValue * 2), 3)),
                      str(int(skillChange + additionalValueChange * 2)) + ';' + str(
                          round(float(valueOfSkill + additionalValue * 3), 3)),
                      str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('vampire'):
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
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"vampire =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill),
                      str(skillChange) + ';' + str(round(valueOfSkill + additionalValue, 3)),
                      str(int(skillChange + additionalValueChange)) + ';' + str(
                          round(valueOfSkill + additionalValue * 2, 3)),
                      str(int(skillChange + additionalValueChange * 2)) + ';' + str(
                          round(valueOfSkill + additionalValue * 3, 3)),
                      str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('longjump'):
                valueOfSkill = random.randrange(110, 600)
                additionalValue = random.randrange(10, 60)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"longjump =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)) + ';' + str(
                        float(valueOfSkill + additionalValue)) + ';' + str(
                        float(valueOfSkill + additionalValue * 2)) + ';' + str(
                        float(valueOfSkill + additionalValue * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('evasion'):
                valueOfSkill = random.randrange(0, 60)
                additionalValue = 0
                if valueOfSkill < 50:
                    additionalValue = random.randrange(3, 7)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"evasion\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(
                          int(valueOfSkill + additionalValue * 2)) + ';' + str(
                          int(valueOfSkill + additionalValue * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('step'):
                valueOfSkill = random.randrange(100, 200)
                additionalValue = random.randrange(5, 20)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"step\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill) + ';' + str(int(valueOfSkill + additionalValue)) + ';' + str(
                          int(valueOfSkill + additionalValue * 2)) + ';' + str(
                          int(valueOfSkill + additionalValue * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('paralyze'):
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
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"paralyze =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange) + ';' + str(float(valueOfSkill + additionalValue)),
                    str(int(skillChange + additionalValueChange)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('invis'):
                additionalValue = 0
                valueOfSkill = random.randrange(0, 100)
                if valueOfSkill < 50:
                    additionalValue = random.randrange(0, 10)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"invis\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(valueOfSkill) + ' me' + ';' + str(
                          int(valueOfSkill + additionalValue)) + ' me' + ';' + str(
                          int(valueOfSkill + additionalValue * 2)) + ' me' + ';' + str(
                          int(valueOfSkill + additionalValue * 3)) + ' me' + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('boom'):
                valueOfSkill = random.randrange(200, 450)
                additionalDamage = 0
                additionalChange = 0
                damage = random.randrange(1, 49)
                change = random.randrange(1, 99)
                if damage <= 10:
                    additionalDamage = random.randrange(1, 8)
                if change < 30:
                    additionalChange = random.randrange(0, 10)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"boom\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(float(valueOfSkill)), str(float(damage)),
                      str(change) + ';' + str(float(valueOfSkill)), str(float(damage + additionalDamage)),
                      str(float(change + additionalChange)) + ';' + str(float(valueOfSkill)),
                      str(float(damage + additionalDamage * 2)),
                      str(int(change + additionalChange * 2)) + ';' + str(float(
                          valueOfSkill)), str(float(damage + additionalDamage * 3)),
                      str(int(change + additionalChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('regen'):
                time: float = random.randrange(1, 10)
                hp = 0
                if time < 5:
                    hp = random.randrange(1, 5)
                elif time >= 5:
                    hp = random.randrange(3, 8)
                additionalHp = random.randrange(1, 3)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"regen\"\n\t\"setting' + str(int(i + 1)) + '\"',
                      '       \"' + str(float(time)), str(hp) + ';' + str(float(time)),
                      str(int(hp + additionalHp)) + ';' + str(float(time)),
                      str(int(hp + additionalHp * 2)) + ';' + str(float(time)), str(int(hp + additionalHp * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('slow'):
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
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"slow =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange) + ';' + str(float(valueOfSkill + additionalValue)),
                    str(int(skillChange + additionalValueChange)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('rockets'):
                amountRocket = random.randrange(1, 4)
                minDamage = random.randrange(1, 20)
                maxDamage = 81
                additionalDamage = random.randrange(1, 20)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"rockets =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(amountRocket), str(minDamage), str(maxDamage) + ';' + str(amountRocket),
                    str(int(minDamage + additionalDamage)), str(maxDamage) + ';' + str(amountRocket),
                    str(int(minDamage + additionalDamage * 2)), str(maxDamage) + ';' + str(amountRocket),
                    str(int(minDamage + additionalDamage * 3)), str(maxDamage) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('mirror'):
                valueOfSkill = random.randrange(100, 250)
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
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"mirror =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange) + ';' + str(round(float(valueOfSkill + additionalValue),3)),
                    str(int(skillChange + additionalValueChange)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('push'):
                valueOfSkill: float = random.randrange(0, 300)
                additionalValue: float = random.randrange(100, 200)
                additionalValue /= 10
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"push =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange) + ';' + str(float(valueOfSkill + additionalValue)),
                    str(int(skillChange + additionalValueChange)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('respawn'):
                valueOfSkill: int = random.randrange(1, 4)
                skillChange = random.randrange(0, 99)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"respawn\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange) + ';' + str(valueOfSkill),
                    str(int(skillChange + additionalValueChange)) + ';' + str(
                valueOfSkill),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str((valueOfSkill)),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('dropweapon'):
                skillChange = random.randrange(0, 99)
                additionalValueChange = 0
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"dropweapon\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(skillChange) + ';' + str(int(skillChange + additionalValueChange)) + ';' +
                    str(int(skillChange + additionalValueChange * 2)) + ';' +
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('blind'):
                valueOfSkill = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                type: int = random.randrange(1, 3)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"blind =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange), str(type) + ';' + str(float(valueOfSkill + additionalValue)),
                    str(int(skillChange + additionalValueChange)), str(type) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))),
                    str(int(skillChange + additionalValueChange * 2)), str(type) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))),
                    str(int(skillChange + additionalValueChange * 3)), str(type) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('poison'):
                time: float = random.randrange(0, 5)
                frequency: float = random.randrange(1, 3)
                damage: float = random.randrange(1, 10)
                change: int = random.randrange(0, 100)
                additionalDamage = random.randrange(1, 2)
                print('\n\t\"skill' + str(int(i + 1)) + '\"          \"poison =\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(time), str(frequency), str(damage), str(change) + ';' + str(time), str(frequency), str(damage+additionalDamage), str(change) + ';' + str(time), str(frequency), str(damage+additionalDamage*2), str(change) + ';' + str(time), str(frequency), str(damage+additionalDamage*3), str(change) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('illusion'):
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
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"illusion\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)),
                    str(skillChange) + ';' + str(float(valueOfSkill + additionalValue)),
                    str(int(skillChange + additionalValueChange)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            elif self.tempList[i] == self.listSkills.index('bury'):
                valueOfSkill = random.randrange(100, 150)
                valueOfSkill /= 100
                additionalValue = random.randrange(100, 500)
                additionalValue /= 1000
                skillChange = random.randrange(0, 100)
                additionalValueChange = 0
                depth: float = random.randrange(0, 101)
                if 30 < skillChange < 50:
                    additionalValueChange = random.randrange(0, 10)
                elif skillChange < 30:
                    additionalValueChange = random.randrange(5, 10)
                elif skillChange == 0:
                    additionalValueChange = random.randrange(10, 15)
                print(
                    '\n\t\"skill' + str(int(i + 1)) + '\"          \"bury\"\n\t\"setting' + str(int(i + 1)) + '\"',
                    '       \"' + str(float(valueOfSkill)), str(depth),
                    str(skillChange) + ';' + str(float(valueOfSkill + additionalValue)), str(depth),
                    str(int(skillChange + additionalValueChange)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 2, 3))), str(depth),
                    str(int(skillChange + additionalValueChange * 2)) + ';' + str(float(
                        round(valueOfSkill + additionalValue * 3, 3))), str(depth),
                    str(int(skillChange + additionalValueChange * 3)) + '\"', end='')
            else:
                print('Error')
            i += 1

    def GenerateUltimate(self):
        cooldown = 0
        z = random.randrange(0, 20)
        if z == self.listUltimate.index('teleport'):
            cooldown = random.randrange(1, 10)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('jetpack'):
            cooldown = random.randrange(1, 10)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('explode'):
            cooldown = random.randrange(30, 50)
            radius:float = random.randrange(10, 300)
            damage:float = random.randrange(5, 49)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), 'aim', str(radius), str(damage) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultfreeze'):
            cooldown = random.randrange(10, 25)
            radius:float = random.randrange(1, 300)
            duration:float = random.randrange(1, 3)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), 'radius', str(radius), str(duration) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('CreateProp'):
            cooldown = random.randrange(1, 5)
            path: str = 'models/props/cs_office/vending_machine.mdl'
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), path +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultgod'):
            cooldown = random.randrange(15, 30)
            duration: float = random.randrange(1, 8)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), str(duration) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('webshot'):
            cooldown = random.randrange(1, 5)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultburn'):
            cooldown = random.randrange(10, 25)
            radius:float = random.randrange(1, 300)
            duration:float = random.randrange(1, 3)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), 'radius', str(radius), str(duration) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('speedbuf'):
            cooldown = random.randrange(10, 25)
            speed: float = random.randrange(250, 400)
            duration: float = random.randrange(1, 5)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), str(speed), str(duration) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('heal'):
            cooldown = random.randrange(1, 5)
            hp: int = random.randrange(20, 150)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), str(hp) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultblind'):
            cooldown = random.randrange(10, 25)
            radius:float = random.randrange(1, 300)
            duration:float = random.randrange(1, 3)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), 'radius', str(radius), str(duration) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultremove'):
            cooldown = random.randrange(10, 25)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultburyme'):
            cooldown = random.randrange(2, 7)
            depth: float = random.randrange(10, 100)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), str(depth) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('fatality'):
            cooldown = random.randrange(15, 25)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('blink'):
            cooldown = random.randrange(25, 35)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('ultswap'):
            cooldown = random.randrange(7, 20)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('sphere'):
            cooldown = random.randrange(15, 25)
            duration: float = random.randrange(1, 8)
            radius: float = random.randrange(10, 400)
            reward = 10
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), str(duration), str(radius), str(reward) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('chaos'):
            cooldown = random.randrange(25, 40)
            damage: float = random.randrange(1, 49)
            durationSlow: float = random.randrange(1, 7)
            durationStun: float = random.randrange(1, 4)
            radius: float = random.randrange(10, 200)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]), damage, durationSlow, durationStun, str(radius) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('teleportator'):
            cooldown = random.randrange(1, 7)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        if z == self.listUltimate.index('portals'):
            cooldown = random.randrange(1, 7)
            print('\n\t\"ultimate\"\t\"' + str(self.listUltimate[z]) +'\"\n\t\"cooldown\"\t\"' + str(cooldown) + '\"', end='')
        print('\n}')


obj = Race()
obj.Input()
obj.DefaultForm()
obj.GenerateSkills()
obj.GenerateParams()
obj.GenerateUltimate()