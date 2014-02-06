'''
Created on 28 jan. 2014

@author: Pieter
'''
from PIL import Image

class Card():
    '''Objectholder for the cards in Dunqeun Petz'''
    standards = {"red":"anger","green":"food","purple":"magic","yellow":"play"} #standard needs for a color

    def __init__(self,color,need):
        '''Card(string color [,string need="standard"]) -> Card
        :param color: Color of the card string
        :param need: type of need, standard for the standard for that color
        '''
        self.color = color
        self.need=need
        self.flipped=False
        if (self.color,self.need) in self.standards.items():
            self.numNeeds=1
        else:
            self.numNeeds=2

    def turnCard(self):
        '''C.turnCard() -- Turns over the card.'''
        self.flipped = not self.flipped

    def getNeeds(self):
        '''C.getNeeds -> list -- returns a list of (1 or 2) need(s)'''
        if not self.flipped:
            return [self.need]
        else:
            if self.numNeeds==1:
                return [self.need]
            else:
                return [self.need,self.standards[self.color]]

    def getCard(self):
        '''C.getCard() -> Image -- returns an Image-object for the card. Rightly Turned'''
        crd = "dungeonz\\artwork\\cards\\"+self.color+"_"+self.need+".png"
        im = Image.open(crd)
        if self.flipped:
            im = im.rotate(180)
        return im








