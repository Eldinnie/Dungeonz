'''
Created on 18 jan. 2014

@author: Pieter
'''
from dungeonz.Cage import Cage, Upgrade
from dungeonz.CageBoard import CageBoard
from dungeonz.Petz import Pet
from PIL import Image
import random
CAGES_STACK = []
UPGRADES_STACK = []
PETZ_STACK=[]
PLAYERS=[]
PLAYER1=0
PLAYER2=1
PLAYER3=2
PLAYER4=3
cage_background = Cage("cage_back.png")
upgrade_background = Upgrade("upgrade_back.png")


def makeCageArray():
    loc = []
    loc.append(Cage("cage_1.png",strength=2,magic=1))
    loc.append(Cage("cage_2.png",strength=1,magic=2))
    loc.append(Cage("cage_3.png",strength=1,magic=1,play=1))
    loc.append(Cage("cage_3.png",strength=1,magic=1,play=1))
    loc.append(Cage("cage_4.png",strength=1,removes_poo=True,supplies_vegetables=True))
    loc.append(Cage("cage_4.png",strength=1,removes_poo=True,supplies_vegetables=True))
    loc.append(Cage("cage_5.png",strength=3))
    loc.append(Cage("cage_5.png",strength=3))
    loc.append(Cage("cage_6.png",magic=3))
    loc.append(Cage("cage_6.png",magic=3))
    loc.append(Cage("cage_7.png",magic=1,play=2))
    return loc


def makeUpgradeArray():
    loc=[]
    loc.append(Upgrade("upgrade_1.png","strength"))
    loc.append(Upgrade("upgrade_1.png","strength"))
    loc.append(Upgrade("upgrade_2.png","magic"))
    loc.append(Upgrade("upgrade_2.png","magic"))
    loc.append(Upgrade("upgrade_3.png","play"))
    loc.append(Upgrade("upgrade_4.png","supplies_meat"))
    return loc

def makePetzArray():
    loc=[]
    loc.append(Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5}))
    loc.append(Pet("2",eating="veg",sell_value={4:2,5:3,6:4,7:5}))
    loc.append(Pet("3",sell_value={4:1,5:2,6:3,7:4}))
    loc.append(Pet("4",eating="meat",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("5",eating="veg",sell_value={4:2,5:3,6:4,7:5}))
    loc.append(Pet("6",eating="veg",sell_value={4:2,5:3,6:4,7:5}))
    loc.append(Pet("7",eating="meat",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("8",eating="veg",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("9",eating="meat",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("10",sell_value={4:1,5:2,6:3,7:4}))
    loc.append(Pet("11",sell_value={4:1,5:2,6:3,7:4}))
    loc.append(Pet("12",sell_value={4:1,5:2,6:3,7:4}))
    loc.append(Pet("13",sell_value={4:1,5:2,6:3,7:4}))
    loc.append(Pet("14",eating="meat",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("15",eating="meat",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("16",eating="meat",sell_value={4:3,5:4,6:5,7:6}))
    loc.append(Pet("17",eating="veg",sell_value={4:2,5:3,6:4,7:5}))
    loc.append(Pet("18",sell_value={4:1,5:2,6:3,7:4}))
    return loc
    
def main():
    preparation()    
    player1=CageBoard(1)
    player1.addCage(2, CAGES_STACK[3])
    player1.addCage(3, CAGES_STACK[2])
    player1.addCage(4, CAGES_STACK[1])
    player1.addUpgrade(1, UPGRADES_STACK[5])
    player1.addUpgrade(2, UPGRADES_STACK[2])
    player1.addUpgrade(3, UPGRADES_STACK[4])
    player1.addUpgrade(4, UPGRADES_STACK[1])
    player1.cages[1].addPoo(3)
    player1.cages[3].addPoo(4)
    player1.cages[2].addPoo()
    player1.getBoard().show()

    
def preparation():
    global CAGES_STACK
    global UPGRADES_STACK
    global PETZ_STACK
    PETZ_STACK=makePetzArray()
    UPGRADES_STACK = makeUpgradeArray()
    CAGES_STACK = makeCageArray()  
    random.shuffle(CAGES_STACK)
    random.shuffle(UPGRADES_STACK)
    random.shuffle(PETZ_STACK) 
    

if __name__ == '__main__':
    main()
