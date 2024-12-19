class Personnage:
    def __init__(self,sprites,xp,yp,deplt):#Constructeur
        self.sprites=sprites
        self.xp=xp
        self.yp=yp
        self.deplt=deplt
        self.index=0
        self.sens='droite'

    def deplacer_droite(self):
        '''Cette fonction fait augmenter le self.xp et renvoie la bonne image'''
        self.sens='droite'
        self.xp +=self.deplt
        self.index = (self.index + 1) % 6
        return self.sprites[self.index]

    def deplacer_gauche(self):
        '''Cette fonction fait diminue le self.xp et renvoie la bonne image'''
        self.sens='gauche'
        self.xp -=self.deplt
        self.index = ((self.index + 1) % 6)+6
        return self.sprites[self.index]

    def stop(self):
        '''Cette fonction renvoie la bonne image en fonction des sens'''
        if self.sens=='droite':
            return self.sprites[12]
        elif self.sens=='gauche':
            return self.sprites[13]
