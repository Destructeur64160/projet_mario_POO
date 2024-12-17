
class Personnage:
    def __init__(self,sprites,xp,yp,deplt):
        self.sprites=sprites
        self.xp=xp
        self.yp=yp
        self.deplt=deplt
        self.index=0
        self.sens='droite'
        self.is_jumping = False  # Nouveau : Mario saute ou non
        self.jump_time = 0
        self.rectangle=sprites[0].get_rect().inflate(-5,-5)
        self.rectangle.topleft = (self.xp, self.yp)

    def deplacer_droite(self):
        self.sens='droite'
        self.xp +=self.deplt
        self.index = (self.index + 1) % 6
        return self.sprites[self.index]
    def deplacer_gauche(self):
        self.sens='gauche'
        self.xp -=self.deplt
        self.index = ((self.index + 1) % 6)+6
        return self.sprites[self.index]
    def stop(self):
        if self.sens=='droite':
            return self.sprites[12]
        elif self.sens=='gauche':
            return self.sprites[13]


class Mario(Personnage):	# la classe Mario hérite de la classe Personnage
    # la déclaration du constructeur de Mario est identique
    # à celle du constructeur de Personnage
    def __init__(self, sprite, xp = 50, yp = 296, deplt = 10):
        # Appel explicite au constructeur de la classe Personnage
        Personnage.__init__(self, sprite, xp = 50, yp = 296, deplt = 10)
        # D’autres propriétés peuvent être rajoutées ici

    def saute(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_velocity = -25  # Vitesse initiale pour monter
            if self.sens == 'droite':
                return self.sprites[16]
            else:
                return self.sprites[17]

