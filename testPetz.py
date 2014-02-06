'''
Created on 5 feb. 2014

@author: Pieter
'''
import unittest
from dungeonz.Petz import Pet
from dungeonz.Cage import Cage

class Test(unittest.TestCase):


    def testConstructor(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        self.assertIsInstance(tp, Pet)
        self.assertEqual(tp.level, 2)
        self.assertEqual(tp.eating, "veg")
        self.assertEqual(tp.sell_value, {4:2,5:3,6:4,7:5})
        del(tp)

    def testLevelUp(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        tp2 = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        tp2.level=3
        self.assertEqual(tp.level, 2)
        self.assertEqual(tp2.level, 3)
        tp.levelUp()
        tp2.levelUp()
        self.assertEqual(tp.level, 4)
        self.assertEqual(tp2.level, 5)
        tp.levelUp()
        tp2.levelUp()
        self.assertEqual(tp.level, 5)
        self.assertEqual(tp2.level, 6)
        tp.levelUp()
        tp2.levelUp()
        self.assertEqual(tp.level, 6)
        self.assertEqual(tp2.level, 7)
        tp.levelUp()
        tp2.levelUp()
        self.assertEqual(tp.level, 7)
        self.assertEqual(tp2.level, 7)
        tp.levelUp()
        tp2.levelUp()
        self.assertEqual(tp.level, 7)
        self.assertEqual(tp2.level, 7)
        del(tp)
        del(tp2)

    def testGetAttributes(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        tp2 = Pet("13",sell_value={4:1,5:2,6:3,7:4})
        tp.levelUp()
        tp2.levelUp()
        tpa=tp.getAttributes()
        tpb=tp2.getAttributes()
        self.assertIsInstance(tpa, dict)
        self.assertIsInstance(tpb, dict)
        self.assertIsInstance(tpa['level'], int)
        self.assertIsInstance(tpb['level'], int)
        self.assertIsInstance(tpa['eating'], str)
        self.assertIsInstance(tpb['eating'], str)
        self.assertIsInstance(tpa['sell_value'], int)
        self.assertIsInstance(tpb['sell_value'], int)
        self.assertEqual(tpa['level'], 4)
        self.assertEqual(tpb['level'], 4)
        self.assertEqual(tpa['eating'], "veg")
        self.assertEqual(tpb['eating'], "omni")
        self.assertEqual(tpa['sell_value'], 2)
        self.assertEqual(tpb['sell_value'], 1)
        tp.levelUp()
        tp.levelUp()
        tp.levelUp()
        tp.levelUp()
        tp2.levelUp()
        tp2.levelUp()
        tp2.levelUp()
        tp2.levelUp()
        tpa=tp.getAttributes()
        tpb=tp2.getAttributes()
        self.assertEqual(tpa['sell_value'], 5)
        self.assertEqual(tpb['sell_value'], 4)

    def testSetLevelTo3(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        self.assertEqual(tp.level, 2)
        tp.setLevelTo3()
        self.assertEqual(tp.level, 3)
        tp.setLevelTo3()
        self.assertEqual(tp.level, 3)

    def testGiveCage(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        tc = Cage("cage_1.png",strength=2,magic=1)
        self.assertEqual(tp.cage, None)
        self.assertTrue(tp.giveCage(tc))
        self.assertEqual(tp.cage, tc)
        self.assertFalse(tp.giveCage(tc))

    def testGetCage(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        tc = Cage("cage_1.png",strength=2,magic=1)
        self.assertEqual(tp.getCage(), None)
        tp.giveCage(tc)
        self.assertEqual(tp.getCage(), tc)

    def testRemoveCage(self):
        tp = Pet("1",eating="veg",sell_value={4:2,5:3,6:4,7:5})
        tc = Cage("cage_1.png",strength=2,magic=1)
        tp.giveCage(tc)
        self.assertEqual(tp.getCage(), tc)
        tp.removeCage()
        self.assertEqual(tp.getCage(), None)
        self.assertEqual(tp.cage, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()