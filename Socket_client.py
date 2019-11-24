#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import pygame


print ("Приветствую Дредд, введи уровень: ")
level:int = input ()
print("Введи ник: ")
name:str = input ()


result: str = "magnus;magnus161;./csgoserver console;wcs_setlblvl " + level + " " + name
print (result)
print ("magnus\nmrmagnus161\n./csgoserver console\nwcs_setlblvl + " + level + " " + name)
input('Press ENTER to exit')

#sock = socket.socket()
#sock.connect(('localhost', 9090))
#sock.send('hello, world!')

#data = sock.recv(1024)
#sock.close()

#print (data)