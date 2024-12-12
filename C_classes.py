

class Personnage:
    def __init__(self,sprites,xp,yp,deplt):
        self.sprites=sprites
        self.xp=xp
        self.yp=yp
        self.deplt=deplt
        self.index=0

    def deplacer_droite(self):
        self.xp +=self.deplt
        self.index = (self.index + 1) % 6
        return self.sprites[self.index]
    def deplacer_gauche(self):
        self.xp -=self.deplt
        self.index = ((self.index + 1) % 6)+6
        return self.sprites[self.index]
    def stop(self, sens):
        if sens=='droite':
            return self.sprites[12]
        elif sens=='gauche':
            return self.sprites[13]

