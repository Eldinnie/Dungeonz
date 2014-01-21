'''
Created on 18 jan. 2014

@author: Pieter
'''
from Cage import Cage
from Petz import Pet
from PIL import Image,ImageFont,ImageDraw

class CageBoard(object):
    '''
    classdocs
    '''

    upgrade_locs=((16,11),(144,11),(16,351),(144,351))
    cages_locs=((16,57),(144,57),(16,216),(144,216))
    petz_locs=((26,67),(154,67),(26,226),(154,226))
    poo_locs=((48,110),(176,110),(48,269),(176,269))
    poo_text_locs=((56,116),(184,116),(56,275),(184,275))
    poo=Image.open("dungeonz\\artwork\\tokens\\poo.png")
    font = ImageFont.truetype("dungeonz\\artwork\\gamefont.ttf", 24)
    def __init__(self,player):
        '''
        Constructor
        '''
        self.cages=[]
        self.cage_upgrades=[]
        self.petz=[]
        self.free=[1,1,1,1]
        self.cages.append(Cage("cage_0.png",1,1))
        self.cages[0].addPoo()
        self.cage_upgrades.append(None)
        self.cage_upgrades.append(None)
        self.cage_upgrades.append(None)
        self.cage_upgrades.append(None)
        self.cages.append(None)
        self.cages.append(None)
        self.cages.append(None)
        self.petz.append(None)
        self.petz.append(None)
        self.petz.append(None)
        self.petz.append(None)
        self.baseboard = Image.open("dungeonz\\artwork\\boards\\cage_board"+str(player)+".jpg")
        self.draw=ImageDraw.Draw(self.baseboard)

    def addCage(self,slot,cage):
        if self.free[slot-1]==1:
            self.cages[slot-1]=cage
            self.free[slot-1]=0
            return True
        else:
            return False

    def addPetToCage(self,pet,slot):
        if self.petz[slot-1]==None:
            self.petz[slot-1]=pet
            pet.giveCage(self)

    def getCage(self,slot):
        return self.cages[slot-1]

    def addUpgrade(self,slot,expansion):
        if (self.cage_upgrades[slot-1]==None) and (self.cages[slot-1] != None):
            print "adding expansion"
            self.cage_upgrades[slot-1]=expansion
            self.cages[slot-1].addUpgrade(expansion.type)
            return True
        else:
            return False

    def getBoard(self):
        for x,cage in enumerate(self.cages):
            if cage != None:
                if x==0 and self.free[0]==1:
                    pass
                else:
                    self.baseboard.paste(cage.getImage(),self.cages_locs[x])
                if self.cage_upgrades[x] != None:
                    self.baseboard.paste(self.cage_upgrades[x].getImage(),self.upgrade_locs[x])
                if self.petz[x] != None:
                    self.baseboard.paste(self.petz[x].getImage(),self.petz_locs[x],self.petz[x].getImage())
                if cage.getPoo()>=1:
                    print cage.getPoo()
                    self.baseboard.paste(self.poo,self.poo_locs[x],self.poo)
                    self.draw.text(self.poo_text_locs[x], str(cage.getPoo()),(0,0,0), font=self.font)
        return self.baseboard

