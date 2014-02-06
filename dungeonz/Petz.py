'''
Created on 19 jan. 2014

@author: Pieter
'''
from PIL import Image  # @UnresolvedImport

class Pet():
    '''
    The Pet class creates the objects for the petz. It holds and tracks information about the following:
    - Image-files
    - Level
    - Eating habits
    - sell-values
    '''
    baseroot_top="dungeonz\\artwork\\petz\\top_"
    baseroot_bottom="dungeonz\\artwork\\petz\\bottom_"
    def __init__(self,image,level=2,eating="omni",sell_value={4:0,5:0,6:0,7:0}):
        '''Pet(string image,[int level=2,[string eating=omni,[dict sell_value={4:0,5:0,6:0,7:0}]]]) -> Pet'''
        self.cage=None
        self.image = image
        self.level = level
        self.eating = eating
        self.sell_value = sell_value

    def levelUp(self):
        '''P.levelUp() -- Levels the pet up, according to the rules of you petz'''
        if self.level==2 or self.level==3:
            self.level +=2
        elif self.level==7:
            pass
        else:
            self.level+=1

    def setLevel(self,level):
        '''P.setLevel() -- Set level (only to distinguish level 2 and 3 petz)'''
        self.level=level

    def giveCage(self,cage):
        '''P.giveCage(Cage) -- Assign a Cage to a Pet'''
        self.cage=cage

    def getCage(self):
        '''p.getCage() -> Cage -- Returns the Cage the pet is in. None if not in Cage'''
        return self.cage

    def getImage(self):
        '''p.getImage() -> Image -- returns PIL Image-object for the pet with correct level'''
        bottom=self.baseroot_bottom+self.image+"_"+str(self.level)+".png"
        top = self.baseroot_top+self.image+".png"
        im=Image.new("RGBA",(85,110))
        bottom_image=Image.open(bottom)
        top_image=Image.open(top)
        im.paste(bottom_image,(0,im.size[1]-bottom_image.size[1]-1),bottom_image)
        im.paste(top_image,(0,0),top_image)
        return im
