import sys, os

class Player:
	def __init__(self, ID, name, cards):
		self.estime = 100
		self.id = ID
		self.name = name
		self.alive  = True
		self.cards = cards
		for card in self.cards:
			card.owner = ID


	def jouer_carte(self, player, paquet):
		os.system("cls")
		i = 0

		print("Cartes de", player.name, end = '\n')

		for card in self.cards:
			print(i,":", card)
			i+=1
		
		print('\n')
		move = "_"

		while move not in "ADP":
			move = input("Entrez A pour attaquer, D pour defendre ou P pour piocher et passer un tour : ").upper()[0]
		
		
		if move == "P":
			if paquet:
				self.cards.append(paquet[0])
				self.cards[-1].owner = self.id
				print(f"Joueur {self.name} a pioché la", paquet[0])
				paquet.pop(0)
			return None
		
		numero = -1
		while not 0<=numero<len(self.cards) and move != "P":
			numero = int(input("Entrez le numero de la carte qui doit effectuer l'action : "))

		if move == "A": self.cards[numero].mode = "ATTAQUE"
		elif move == "D": self.cards[numero].mode = "DEFENSE"
		
		carte = self.cards[numero]	#Carte choisie
		self.cards.pop(numero)	#Retirer la carte choisie de la main

		print(f"Carte n° {numero}", file = sys.stderr)
		
		return carte


	def interact_with_cards(self, carte):
		"""Intéractions entre joueurs et cartes"""
		
		if carte.mode== "ATTAQUE" and carte.owner != self.id:
			self.estime -= carte.pts_attaque
			if self.estime < 0: self.estime = 0

		if carte.mode == "DEFENSE" and carte.owner == self.id:
		 	self.estime += carte.pts_defense

	def maj_vie(self):
		if self.estime <= 0:
			self.alive = False


		



class Carte:
	def __init__(self, name, pts_defense, pts_attaque, ID):
		self.name = name
		self.pts_defense = pts_defense
		self.pts_attaque = pts_attaque
		self.played = False
		self.mode = ""
		self.owner = ID

		
	def attaque_speciale(self):
		pass

	def __str__(self):
		return f"carte {self.name} : attaque -> {self.pts_attaque} | defense -> {self.pts_defense}"


class Prof(Carte):
	def __init__(self, name, pts_vie, pts_attaque):
		super(Prof, self).__init__(name, 50, 5)

