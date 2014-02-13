'''
Created on 7 feb. 2014

@author: Pieter
'''
import unittest
from dungeonz.CageBoard import CageBoard
from dungeonz.Cage import Cage, Upgrade
from dungeonz.Petz import Pet

class Test(unittest.TestCase):

    def setUp(self):
        self.cb1 = CageBoard(1)
        self.cb2 = CageBoard(2)
        self.cb3 = CageBoard(3)
        self.cb4 = CageBoard(4)
        self.tc1 = Cage("cage_1.png",strength=2,magic=1)
        self.tc2 = Cage("cage_6.png",magic=3)
        self.tu=Upgrade("upgrade_1.png", "strength")
        self.tp=Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})

    def tearDown(self):
        del(self.cb1)
        del(self.cb2)
        del(self.cb3)
        del(self.cb4)
        del(self.tc1)
        del(self.tc2)
        del(self.tu)
        del(self.tp)

    def testConstructor(self):
        self.assertIsInstance(self.cb1, CageBoard)
        self.assertIsInstance(self.cb1.cages, list)
        self.assertIsInstance(self.cb1.cages[0], Cage)
        self.assertEqual(self.cb1.cages[1], None)
        self.assertEqual(self.cb1.cages[2], None)
        self.assertEqual(self.cb1.cages[3], None)
        self.assertIsInstance(self.cb1.cage_upgrades, list)
        self.assertEqual(self.cb1.cage_upgrades, [None,None,None,None])
        self.assertIsInstance(self.cb1.petz, list)
        self.assertEqual(self.cb1.petz, [None,None,None,None])
        self.assertIsInstance(self.cb1.free, list)
        self.assertEqual(self.cb1.free, [1,1,1,1])
        self.assertEqual(self.cb1.cages[0].getAttributes()['poo'], 1)

        self.assertIsInstance(self.cb2, CageBoard)
        self.assertIsInstance(self.cb2.cages, list)
        self.assertIsInstance(self.cb2.cages[0], Cage)
        self.assertEqual(self.cb2.cages[1], None)
        self.assertEqual(self.cb2.cages[2], None)
        self.assertEqual(self.cb2.cages[3], None)
        self.assertIsInstance(self.cb2.cage_upgrades, list)
        self.assertEqual(self.cb2.cage_upgrades, [None,None,None,None])
        self.assertIsInstance(self.cb2.petz, list)
        self.assertEqual(self.cb2.petz, [None,None,None,None])
        self.assertIsInstance(self.cb2.free, list)
        self.assertEqual(self.cb2.free, [1,1,1,1])
        self.assertEqual(self.cb2.cages[0].getAttributes()['poo'], 1)

        self.assertIsInstance(self.cb3, CageBoard)
        self.assertIsInstance(self.cb3.cages, list)
        self.assertIsInstance(self.cb3.cages[0], Cage)
        self.assertEqual(self.cb3.cages[1], None)
        self.assertEqual(self.cb3.cages[2], None)
        self.assertEqual(self.cb3.cages[3], None)
        self.assertIsInstance(self.cb3.cage_upgrades, list)
        self.assertEqual(self.cb3.cage_upgrades, [None,None,None,None])
        self.assertIsInstance(self.cb3.petz, list)
        self.assertEqual(self.cb3.petz, [None,None,None,None])
        self.assertIsInstance(self.cb3.free, list)
        self.assertEqual(self.cb3.free, [1,1,1,1])
        self.assertEqual(self.cb3.cages[0].getAttributes()['poo'], 1)

        self.assertIsInstance(self.cb4, CageBoard)
        self.assertIsInstance(self.cb4.cages, list)
        self.assertIsInstance(self.cb4.cages[0], Cage)
        self.assertEqual(self.cb4.cages[1], None)
        self.assertEqual(self.cb4.cages[2], None)
        self.assertEqual(self.cb4.cages[3], None)
        self.assertIsInstance(self.cb4.cage_upgrades, list)
        self.assertEqual(self.cb4.cage_upgrades, [None,None,None,None])
        self.assertIsInstance(self.cb4.petz, list)
        self.assertEqual(self.cb4.petz, [None,None,None,None])
        self.assertIsInstance(self.cb4.free, list)
        self.assertEqual(self.cb4.free, [1,1,1,1])
        self.assertEqual(self.cb4.cages[0].getAttributes()['poo'], 1)

    def testAddCage(self):
        self.assertIsInstance(self.cb1.cages[0], Cage)
        self.assertEqual(self.cb1.free, [True for x in range(4)])  # @UnusedVariable
        self.assertFalse(self.cb1.addCage(1, " tralala"))
        self.assertFalse(self.cb1.addCage(6, self.tc1))
        self.assertTrue(self.cb1.addCage(1, self.tc1))
        self.assertEqual(self.cb1.free, [False,True,True,True])
        self.assertEqual(self.cb1.cages[0], self.tc1)
        self.assertFalse(self.cb1.addCage(1, self.tc2))
        self.assertEqual(self.cb1.cages[0], self.tc1)

    def testGetAttributes(self):
        self.assertIsInstance(self.cb1.getAttributes(),dict)
        aa=self.cb1.getAttributes()
        self.assertIsInstance(aa['cages'], list)
        self.assertIsInstance(aa['cage_upgrades'], list)
        self.assertIsInstance(aa['petz'], list)
        self.assertIsInstance(aa['free'], list)
        self.assertEqual(len(aa['cages']), 4)
        self.assertEqual(len(aa['cage_upgrades']), 4)
        self.assertEqual(len(aa['petz']), 4)
        self.assertEqual(len(aa['free']), 4)
        self.assertFalse(self.cb1.getAttributes(5))
        self.assertIsInstance(self.cb1.getAttributes(3),dict)
        self.cb1.addCage(2, self.tc1)
        self.cb1.cage_upgrades[1] = self.tu
        self.cb1.petz[1] = self.tp
        s2= self.cb1.getAttributes(2)
        self.assertEqual(s2['cage'], self.tc1)
        self.assertEqual(s2['cage_upgrade'], self.tu)
        self.assertEqual(s2['pet'], self.tp)
        self.assertFalse(s2['free'])
        
    def testAddPetToCage(self):
        self.cb1.addCage(2, self.tc1)
        self.assertEqual(self.cb1.getAttributes(2)['pet'], None)
        self.assertFalse(self.cb1.addPetToCage(5, self.tp))
        self.assertFalse(self.cb1.addPetToCage(4, self.tp))
        self.assertTrue(self.cb1.addPetToCage(2, self.tp))
        self.assertFalse(self.cb1.addPetToCage(3, "tralala"))
        self.assertEqual(self.cb1.getAttributes(2)['pet'], self.tp)
        self.assertEqual(self.tp.getCage(), self.tc1)
        self.assertFalse(self.cb1.addPetToCage(2, self.tp))
        
    def testAddUpgrade(self):
        self.assertEqual(self.tc1.strength, 2)
        self.assertFalse(self.cb1.addUpgrade(5, self.tu))
        self.assertFalse(self.cb1.addUpgrade(1, "trat"))
        self.assertFalse(self.cb1.addUpgrade(3, self.tu))
        self.assertTrue(self.cb1.addCage(2, self.tc1))
        self.assertTrue(self.cb1.addUpgrade(2, self.tu))
        self.assertEqual(self.tc1.strength, 3)
        self.assertFalse(self.cb1.addUpgrade(2, self.tu))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()