#Classes methods
class Edibles:
    def __init__(self):
        pass
    def setVegetables(self,veggie):
        self.a = veggie
    def setFruits(self,fruit):
        self.b = fruit
    def setBakery(self,bake):
        self.c = bake
    def show(self):
        self.show = ('I like {}, {} and {} very much.'.format(self.a,self.b,self.c))
        print(self.show)
