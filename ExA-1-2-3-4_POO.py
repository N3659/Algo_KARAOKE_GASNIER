from random import*

#on cree la liste de chansons et la variable de score individuel

Chans = [0,1,2,3,4]
ChansIndi = 0
score = random.randint(50,100)

#le joueur choisi aleatoirement un pseudo
choixP = input()

if choixP== 1:
    pseudo = "Monster"

if choixP== 2:
    pseudo = "Billy"

if choixP== 3:
    pseudo = "Lala"

if choixP== 5:
    pseudo = "DarkVador"

if choixP== 5:
    pseudo = "Bob l'éponge"

#creation de la class player

class Player :
    def __init__(self,pseudo,Chans):
        self.name = pseudo
        self.score = Chans

    def getChans(self):
        return self.Chans



#on laisse le joueur choisir une chanson
print (Chans)
print ("choisissez une chanson")
choixC = input()


if choixC == 1:
    Chans[0]

if choixC == 1:
    Chans[1]

if choixC == 1:
    Chans[2]

if choixC == 1:
    Chans[3]

if choixC == 1:
    Chans[4]

J1 = Player(pseudo, choixC, score)
#On utilise la classe pour faire le score d'un des joueurs sur une des chansons