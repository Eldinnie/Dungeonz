'''
Created on 18 jan. 2014

@author: Pieter
'''
from Cage import Cage, Upgrade
from Petz import Pet
from PIL import Image,ImageFont,ImageDraw  # @UnresolvedImport

class CageBoard():
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
        self.cages=[None]*4
        self.cage_upgrades=[None]*4
        self.petz=[None]*4
        self.free=[True,True,True,True]
        self.cages[0]=Cage("cage_0.png",1,1)
        self.cages[0].addPoo()
        self.baseboard = Image.open("dungeonz\\artwork\\boards\\cage_board"+str(player)+".jpg")
        self.draw=ImageDraw.Draw(self.baseboard)

    def getAttributes(self,slot=None):
        '''CB.getAttributes([slot = None]) -> dict -- Returns a dict with all values (for selected slot or all) except image'''
        if not slot:
            return {'cages':self.cages,
                    'cage_upgrades':self.cage_upgrades,
                    'petz':self.petz,
                    'free':self.free}
        elif 0<slot<5:
            di=slot-1
            return {'cage':self.cages[di],
                    'cage_upgrade':self.cage_upgrades[di],
                    'pet':self.petz[di],
                    'free':self.free[di]}
        else:
            return False

    def addCage(self,slot,cage):
        '''CB.addCage(int,Cage) --> Boolean -- Adds the supplied Cage-object to int slot. -> False if failed'''
        if 0<slot<5 and self.free[slot-1] and isinstance(cage, Cage):
            self.cages[slot-1]=cage
            self.free[slot-1]=False
            return True
        else:
            return False

    def addPetToCage(self,slot,pet):
        '''CB.addPetToCage(int,Pet) -> Boolean -- Adds a supplied pet-object to a cage on slot int on the board. -> False if failed'''
        if 0<slot<5 and self.petz[slot-1]==None and self.cages[slot-1] != None and isinstance(pet, Pet):
            self.petz[slot-1]=pet
            pet.giveCage(self.cages[slot-1])
            return True
        else:
            return False

    def addUpgrade(self,slot,expansion):
        '''CB.addUpgrade(int,Upgrade) -> Boolean -- Adds a supplied Upgrade-object to slot int. -> False if failed'''
        if (0<slot<5) and (self.cage_upgrades[slot-1]==None) and (self.cages[slot-1] != None) and isinstance(expansion, Upgrade):
            self.cage_upgrades[slot-1]=expansion
            self.cages[slot-1].addUpgrade(expansion)
            return True
        else:
            return False

    def getBoard(self):
        '''CB.getBoard() -> Image -- Returns a PIL Image-object of the full-drawn board. Including: cages, upgrades, petz and poo'''
        for x,cage in enumerate(self.cages):
            if cage != None:
                if x==0 and self.free[0]:
                    pass
                else:
                    self.baseboard.paste(cage.getImage(),self.cages_locs[x])
                if self.cage_upgrades[x] != None:
                    self.baseboard.paste(self.cage_upgrades[x].getImage(),self.upgrade_locs[x])
                if self.petz[x] != None:
                    self.baseboard.paste(self.petz[x].getImage(),self.petz_locs[x],self.petz[x].getImage())
                if cage.getAttributes()['poo']>=1:
                    self.baseboard.paste(self.poo,self.poo_locs[x],self.poo)
                    self.draw.text(self.poo_text_locs[x], str(cage.getAttributes()['poo']),(0,0,0), font=self.font)
        return self.baseboard

