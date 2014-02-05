'''
Created on 18 jan. 2014

@author: Pieter
'''
from Cage import Cage
from PIL import Image,ImageFont,ImageDraw  # @UnresolvedImport

class CageBoard(object):
    '''
    The CageBoard is the main placeholder for Everything concerning cages, upgrades and petz.
    The cages are assigned to a slot (1-4) on the cageboard, and so are upgrades.
    Petz can be added to a slot and will be put in a cage.
    Also contains methods for getting an Image-object to show
    '''

    upgrade_locs=((16,11),(144,11),(16,351),(144,351))
    cages_locs=((16,57),(144,57),(16,216),(144,216))
    petz_locs=((26,67),(154,67),(26,226),(154,226))
    poo_locs=((48,110),(176,110),(48,269),(176,269))
    poo_text_locs=((56,116),(184,116),(56,275),(184,275))
    poo=Image.open("dungeonz\\artwork\\tokens\\poo.png")
    font = ImageFont.truetype("dungeonz\\artwork\\gamefont.ttf", 24)
    def __init__(self,player):
        '''CageBoard(int) -> CageBoard-- int must be the player. This chooses wich mainboard to use.'''
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
        '''CB.addCage(int,Cage) --> Boolean -- Adds the supplied Cage-object to int slot. -> False if failed'''
        if self.free[slot-1]==1:
            self.cages[slot-1]=cage
            self.free[slot-1]=0
            return True
        else:
            return False

    def addPetToCage(self,slot,pet):
        '''CB.addPetToCage(int,Pet) -> Boolean -- Adds a supplied pet-object to a cage on slot int on the board. -> False if failed'''
        if self.petz[slot-1]==None and self.cages[slot-1] != None:
            return True
            self.petz[slot-1]=pet
            pet.giveCage(self.cages[slot-1])
        else:
            return False

    def getCage(self,slot):
        '''CB.getCage(int) -> Cage-object -- Returns the Cageobject for slot int (None if no cage)'''
        return self.cages[slot-1]

    def addUpgrade(self,slot,expansion):
        '''CB.addUpgrade(int,Upgrade) -> Boolean -- Adds a supplied Upgrade-object to slot int. -> False if failed'''
        if (self.cage_upgrades[slot-1]==None) and (self.cages[slot-1] != None):
            print "adding expansion"
            self.cage_upgrades[slot-1]=expansion
            self.cages[slot-1].addUpgrade(expansion.type)
            return True
        else:
            return False

    def getBoard(self):
        '''CB.getBoard() -> Image -- Returns a PIL Image-object of the full-drawn board. Including: cages, upgrades, petz and poo'''
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

