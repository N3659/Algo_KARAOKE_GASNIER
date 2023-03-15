
class Karaoke :

    class Player :
        def __init__(self,nombre,pseudo,score):
            self.nombre = nombre
            self.name = pseudo
            self.score = score
    
        def getScore(self):
            return self.score