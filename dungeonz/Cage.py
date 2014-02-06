'''
Created on 18 jan. 2014

@author: Pieter
'''
from PIL import Image  # @UnresolvedImport


class CageFrame():
    '''Container class for the general imageobject
    for cages and cage upgrades
    '''
    def __init__(self):
        pass

    def getImage(self):
        '''C.getImage() -> PIL Image -- Returns the Image object for the Cage'''
        return self.image

    def showImage(self):
        '''C.showImage() -- Shows the Image. Mainly debugging pupose'''
        self.image.show()

class Cage(CageFrame):
    '''Contains all the information for a Cage.'''
    def __init__(self,image,strength=0,magic=0,play=0,supplies_vegetables=False,
                 supplies_meat=False,removes_poo=False):
        '''Cage(string image,[int strength=0,[int magic=0,[int play=0,[Boolean supplies_vegetables=False,[Boolean supplies_meat=False,[Boolean removes_poo=False]]]]]]) -> Cage'''
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

    def addUpgrade(self, upgrade):
        '''C.addUpgrade(Upgrade) -> bool -- string contains type of upgrade. The value added by the expansion is added to the cages main value. Returns False is failed'''
        attr = upgrade.type
        if self.expanded==False:
            if attr=="strength":
                self.strength+=1
                self.expanded=True
            elif attr=="magic":
                self.magic+=1
                self.expanded=True
            elif attr=="play":
                self.play += 1
                self.expanded=True
            elif attr=="supplies_meat":
                self.supplies_meat=True
                self.expanded=True
            else:
                return False
            return True
        else:
            return False

    def addPoo(self,amount=1):
        '''C.addPoo([int amount=1]) -> bool -- Increases cages poo by amount int assumes positive integer. False if failed'''
        if amount > 0:
            self.poo_in_cage+=amount
            return True
        else:
            return False

    def cleanPoo(self,amount=1):
        '''C.cleanPoo([int amount=1]) -> bool -- Decreases cages' poo by amount. Assumes positive integer, smaller or equal too poo in cage. False if failed.'''
        if amount>self.poo_in_cage or amount < 0:
            return False
        else:
            self.poo_in_cage -= amount
            return True

    def getAttributes(self):
        '''C.getAttributes() -> Dictionary -- Returns a dictionary with all attributes for this cage'''
        retdict={}
        retdict['strength']=self.strength
        retdict['magic']=self.magic
        retdict['play']=self.play
        retdict['supplies_vegetables']=self.supplies_vegetables
        retdict['supplies_meat']=self.supplies_meat
        retdict['removes_poo']=self.removes_poo
        retdict['poo']=self.poo_in_cage
        return retdict

class Upgrade(CageFrame):
    '''Contains information about Cage upgrades
    Mainly image and type
    '''
    def __init__(self,image,need=None):
        '''Upgrade(string image, string need) -> Upgrade'''
        tmpimage = "dungeonz\\artwork\\upgrades\\"+image
        self.image= Image.open(tmpimage)
        self.type=need

