'''
Created on 18 jan. 2014

@author: Pieter
'''
from dungeonz.Cage import Cage, Upgrade
from dungeonz.CageBoard import CageBoard
from dungeonz.Petz import Pet
from dungeonz.Card import Card
import random

CAGES_STACK = []
UPGRADES_STACK = []
PETZ_STACK=[]
CARDS=[[],[],[],[],[]]
RED = 0
GREEN=1
YELLOW=2
PURPLE=3
BLUE=4
PLAYERS=[]
PLAYER1=0
PLAYER2=1
PLAYER3=2
PLAYER4=3
cage_background = Cage("cage_back.png")
upgrade_background = Upgrade("upgrade_back.png")


def makeCageStack():
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

def makeUpgradeStack():
    loc=[]
    loc.append(Upgrade("upgrade_1.png","strength"))
    loc.append(Upgrade("upgrade_1.png","strength"))
    loc.append(Upgrade("upgrade_2.png","magic"))
    loc.append(Upgrade("upgrade_2.png","magic"))
    loc.append(Upgrade("upgrade_3.png","play"))
    loc.append(Upgrade("upgrade_4.png","supplies_meat"))
    return loc

def makePetzStack():
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
    testers()
    
def makeCardsStack():
    tmpgr = {"food":16,"poop":10,"anger":4,"dissease":2}
    for need,count in tmpgr.items():
        for x in range(count):  # @UnusedVariable
            CARDS[GREEN].append(Card("green",need))
    del(tmpgr)
    random.shuffle(CARDS[GREEN])
    tmprd = {"anger":12,"play":4,"food":3,"poop":3,"dissease":2}
    for need,count in tmprd.items():
        for x in range(count):  # @UnusedVariable
            CARDS[RED].append(Card("red",need))
    del(tmprd)
    random.shuffle(CARDS[RED])
    tmpyl={"play":12,"magic":4,"food":2,"poop":2,"dissease":4}
    for need,count in tmpyl.items():
        for x in range(count):  # @UnusedVariable
            CARDS[YELLOW].append(Card("yellow",need))
    del(tmpyl)
    random.shuffle(CARDS[YELLOW])
    tmppl={"magic":12,"anger":4,"play":4,"dissease":4}
    for need,count in tmppl.items():
        for x in range(count):  # @UnusedVariable
            CARDS[PURPLE].append(Card("purple",need))
    del(tmppl)
    random.shuffle(CARDS[PURPLE])
    


def preparation():
    global CAGES_STACK
    global UPGRADES_STACK
    global PETZ_STACK
    global CARDS
    makeCardsStack()
    PETZ_STACK=makePetzStack()
    UPGRADES_STACK = makeUpgradeStack()
    CAGES_STACK = makeCageStack()  
    random.shuffle(CAGES_STACK)
    random.shuffle(UPGRADES_STACK)
    random.shuffle(PETZ_STACK) 
    
def testers():
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
    print CARDS[GREEN][0].color,CARDS[GREEN][0].need,CARDS[GREEN][0].numNeeds
    print CARDS[RED][0].color,CARDS[RED][0].need,CARDS[RED][0].numNeeds
    print CARDS[YELLOW][0].color,CARDS[YELLOW][0].need,CARDS[YELLOW][0].numNeeds
    print CARDS[PURPLE][0].color,CARDS[PURPLE][0].need,CARDS[PURPLE][0].numNeeds
    CARDS[GREEN][0].getCard().show()
    CARDS[GREEN][0].turnCard()
    print CARDS[GREEN][0].flipped
    CARDS[GREEN][0].getCard().show()
    
    
if __name__ == '__main__':
    main()
