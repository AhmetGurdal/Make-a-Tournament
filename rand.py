#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp1254 -*-
import random
print "INSTRUCTIONS"
print "-------------------------------------------------------------"
print "-This is a program for chose players randomly in a tournament."
print "-First you have to insert all players name."
print "-Then you have to insert players who win their game."
print "-When all player's names added ,type 'end' to finish adding."
print "-If first player win the game press 1"
print "-If other one win the game press 2"
print "-For Example 'PlayerA -- PlayerB' is one of chosen players."
print "-If PlayerA won the game type 1"
print "-Else type 2"
print "--------------------------------------------------------------"
liste = []
while True:
	player = raw_input("Insert Player Name:")
	if player == "end":
		break
	else:
		liste.append(player)

retry = []
for i in liste:
	retry.append(i)
next = []
while True:
	liste2 = []
	while True:
		winlist = []
		while len(liste) >= 2:
			a = random.randint(0,len(liste) - 1)
			b = random.randint(0,len(liste) - 1)
			if a == b:
				continue
			playera = liste[a]
			playerb = liste[b]
			if len(next) != 0:
				for i in next:
					if i in liste:
						playera = i
			if playera == playerb:
				while playera == playerb:
					playerb = liste[random.randint(0,len(liste) - 1)]
			print playera + "--" + playerb
			liste.remove(playera)
			liste.remove(playerb)
			liste2.append(playera)
			liste2.append(playerb)
		if len(liste) == 1:
			next.append(liste[0])
			winlist.append(liste[0])
			print "Next tour : " + liste[0]
		liste3 = liste2	
		print "-------------"
		while len(liste2) >= 2:
			who = raw_input(liste2[0] + "--" + liste2[1] + ":")
			if who == "1":
				winlist.append(liste2[0])
				liste2.remove(liste2[0])
				liste2.remove(liste2[0])
				
			
			elif who == "2":
				winlist.append(liste2[1])
				liste2.remove(liste2[0])
				liste2.remove(liste2[0])
				
			else:
				continue
		if len(winlist) == 1:
			print "The winner is " + winlist[0]
			break
		elif len(liste2) == 0:
			print "---------------"
			liste = winlist
		else:
			print "---------------"
			winlist.append(liste2[0])
			liste = winlist
	print "GAME OVER"
	ret = raw_input("Do you wanna restart with Same players? (y/n):")
	if ret == "y" or ret == "Y":
		for i in retry:
			liste.append(i)
		print "--------------"
	else:
		print "I hope u enjoyed"
		break
