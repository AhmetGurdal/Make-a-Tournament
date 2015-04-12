import random
print "-This is a program to chose players randomly in a tournament."
print "-First you have to insert all players name."
print "-Then you have to insert players who win their game."
print "-If first player win the game press a or B"
print "-If other one win the game press b or B"
print "-For Example 'PlayerA -- PlayerB' is one of chosen players."
print "-If PlayerA won the game type a or A"
print "-Else type b or B"
liste = []
while True:
	player = raw_input("Insert Player Name:")
	if player == "end":
		break
	else:
		liste.append(player)

yeni = liste
while True:
	liste = yeni
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
			print playera + "--" + playerb
			liste.remove(playera)
			liste.remove(playerb)
			liste2.append(playera)
			liste2.append(playerb)
		if len(liste) == 1:
			winlist.append(liste[0])
			print "Next tour : " + liste[0]
		liste3 = liste2	
		print "-------------"
		while len(liste2) >= 2:
			who = raw_input(liste2[0] + "--" + liste2[1] + ":")
			if who == "a" or who == "A":
				winlist.append(liste2[0])
				liste2.remove(liste2[0])
				liste2.remove(liste2[0])
				
			
			elif who == "b" or who == "B":
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
	ret = raw_input("Retry? (r/R):")
	if ret == "r" or ret == "R":
		print "Same players"
		print "--------------"
	else:
		break
