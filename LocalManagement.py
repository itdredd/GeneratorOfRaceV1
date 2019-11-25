#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

print("Приветствую Дредд, введи сумму: ")
sum = int(input())
print("Введи ник: ")
name: str = input()
print("Введи скидку: ")
discountLevel = int(input())

totalLvl = (sum * 6 / 100) * (100 + discountLevel)
if 100 <= sum < 200:
    totalLvl += 50
if 200 <= sum < 500:
    totalLvl += 100
if 500 <= sum < 1000:
    totalLvl += 450
if sum >= 1000:
    totalLvl += 800

# result: str = "magnus;magnus161;./csgoserver console;wcs_setlblvl " + str(totalLvl) + " " + name
# print (result)
print("magnus\nmrmagnus161\n./csgoserver console\nwcs_setlblvl + " + str(totalLvl) + " " + name)
input('Press ENTER to exit')

# sock = socket.socket()
# sock.connect(('localhost', 9090))
# sock.send('hello, world!')

# data = sock.recv(1024)
# sock.close()

# print (data)
