scores = [0,1,2,3,4]

print ("Quel est votre nom ?")

input()

pseudo = input()

class Player :
    def __init__(self,pseudo,score):
        self.name = pseudo
        self.score = score

    def getScore(self):
        return self.score
