'''
Created on 18 jan. 2014

@author: Pieter
'''
from PIL import Image

class CageFrame(object):
    '''
    Container class for the general imageobject
    for cages and cage upgrades
    '''    
    def __init__(self):
        pass
    
    def getImage(self):
        '''
        Returns the Image object for the tile
        '''
        return self.image
    
    def showImage(self):
        '''
        Shows the Image. Mainly debugging pupose
        '''
        self.image.show()

class Cage(CageFrame):
    '''
    Contains all the information for a Cage.
    '''
    def __init__(self,image,strength=0,magic=0,play=0,supplies_vegetables=False,
                 supplies_meat=False,removes_poo=False):
        tmpimage = "dungeonz\\artwork\\cages\\"+image
        self.image= Image.open(tmpimage)
        self.strength=strength
        self.magic=magic
        self.play=play
        self.supplies_vegetables=supplies_vegetables
        self.supplies_meat=supplies_meat
        self.removes_poo=removes_poo
        self.expanded=False
        self.poo_in_cage=0

    def addUpgrade(self, attr):
        '''
        Adds an expansion to a cage.
        The value added by the expansion is added to the cages main value
        '''
        if attr=="strength":
            self.strength+=1
        elif attr=="magic":
            self.magic+=1
        elif attr=="play":
            self.play += 1
        elif attr=="supplies_meat":
            self.supplies_meat=True
        else:
            print "Unknown expansion attribute"
        self.expanded=True
        
    def addPoo(self,amount=1):
        '''
        Pets poo
        '''
        self.poo_in_cage+=amount
    
    def getPoo(self):
        return self.poo_in_cage

    def __repr__(self):
        '''
        debugging
        '''
        retstr = "Strength: "+str(self.strength)+"\n"
        retstr+= "Magic resistance: "+str(self.magic)+"\n"
        retstr+= "Play attributes: "+str(self.play)+"\n"
        retstr+= "Supplies vegetables "+str(self.supplies_vegetables)+"\n"
        retstr+= "Supplies Meat: "+str(self.supplies_meat)+"\n"
        retstr+= "Removes Poo: "+str(self.removes_poo)+"\n"
        retstr+= "Expanded: "+str(self.expanded)+"\n"
        retstr+= "Poo in cage: "+str(self.poo_in_cage)
        return retstr
    
   
        
class Upgrade(CageFrame):
    '''
    Contains information about Cage upgrades
    Mainly image and type
    '''
    def __init__(self,image,type=None):
        tmpimage = "dungeonz\\artwork\\upgrades\\"+image
        self.image= Image.open(tmpimage)
        self.type=type
    
    
    
