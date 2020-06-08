from Class import *
from random import randint 

#Fonctions 

def distribuerUneMain():
	cards = []
	for i in range(5):
		cards.append(Carte(str(i), randint(15, 50), randint(2, 7), randint(500, 5000)))
	return cards
		
def partie_en_cours(players, paquet):
	if len([*filter(lambda p: p.alive, players)]) <= 1: return False
	if len(paquet)==0: return False
	return True


def afficher_la_partie(players, plateau, playerName=""):
	for player in players:
		print("Le joueur", player.name, "a", player.estime,"points de confiance en soi")
	print ("Il reste", len(paquet), "cartes dans le paquet.")
	if playerName: print("C'est au tour de", playerName, "de jouer")


def extract_played_cards(plateau, cartes_a_terre):
	for carte in plateau:
		if carte.tours_restants == 0:
			carte.played = True
			paquet.remove(carte)
			cartes_a_terre.append(carte)
		else:
			carte.tours_restants -= 1

#-------------------------------------
#main :

#Initialisations
players = []
cartes_a_terre = []
plateau = []
paquet = []

for i in range(15):
	paquet.append(Carte(str(i), randint(15, 30), randint(2, 15), -1))


for i in range(int(input("Combien de joueurs: " ))):
	name = input("Nom ? ")
	players.append(Player(i, name, distribuerUneMain()))

#boucle de jeu
while partie_en_cours(players, paquet):	
	
	for player in players:
		afficher_la_partie(players, plateau, player.name)
		input()
		carte = player.jouer_carte(player, paquet)
		if carte: plateau.append(carte)

	for card in plateau:
		for player in players:
			if not player.alive: players.remove(player)
			else: player.interact_with_cards(card)
				
	for player in players: player.maj_vie()
	extract_played_cards(plateau, cartes_a_terre)

print(max(players, key = lambda p: p.estime).name,"est le grand gagnant !")
input()
