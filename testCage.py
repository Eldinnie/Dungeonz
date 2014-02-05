'''
Created on 5 feb. 2014

@author: Pieter
'''
import unittest
from dungeonz.Cage import Cage,Upgrade

class TestCage(unittest.TestCase):


    def setUp(self):
        self.testCage1=Cage("cage_1.png",strength=2,magic=1)
        self.testCage2=Cage("cage_3.png",strength=1,magic=1,play=1)
        self.testCage3=Cage("cage_4.png",strength=1,removes_poo=True,supplies_vegetables=True)
        self.testUpgrade1=Upgrade("upgrade_1.png","strength")
        self.testUpgrade2=Upgrade("upgrade_3.png","play")
        self.testUpgrade3=Upgrade("upgrade_2.png","magic")
        self.testUpgrade4=Upgrade("upgrade_4.png","supplies_meat")


    def tearDown(self):
        del(self.testCage1)
        del(self.testCage2)
        del(self.testCage3)
        del(self.testUpgrade1)
        del(self.testUpgrade2)
        del(self.testUpgrade3)
        del(self.testUpgrade4)


    def testCageTypes(self):
        self.assertIsInstance(self.testCage1, Cage)
        self.assertIsInstance(self.testCage2, Cage)
        self.assertIsInstance(self.testCage3, Cage)

    def testCageAttributeTypes(self):
        self.assertIn("strength", self.testCage1.getAttributes().keys())
        self.assertIn("magic", self.testCage1.getAttributes().keys())
        self.assertIn("play", self.testCage1.getAttributes().keys())
        self.assertIn("supplies_vegetables", self.testCage1.getAttributes().keys())
        self.assertIn("supplies_meat", self.testCage1.getAttributes().keys())
        self.assertIn("removes_poo", self.testCage1.getAttributes().keys())
        self.assertIn("poo", self.testCage1.getAttributes().keys())

        self.assertIn("strength", self.testCage2.getAttributes().keys())
        self.assertIn("magic", self.testCage2.getAttributes().keys())
        self.assertIn("play", self.testCage2.getAttributes().keys())
        self.assertIn("supplies_vegetables", self.testCage2.getAttributes().keys())
        self.assertIn("supplies_meat", self.testCage2.getAttributes().keys())
        self.assertIn("removes_poo", self.testCage2.getAttributes().keys())
        self.assertIn("poo", self.testCage2.getAttributes().keys())

        self.assertIn("strength", self.testCage3.getAttributes().keys())
        self.assertIn("magic", self.testCage3.getAttributes().keys())
        self.assertIn("play", self.testCage3.getAttributes().keys())
        self.assertIn("supplies_vegetables", self.testCage3.getAttributes().keys())
        self.assertIn("supplies_meat", self.testCage3.getAttributes().keys())
        self.assertIn("removes_poo", self.testCage3.getAttributes().keys())
        self.assertIn("poo", self.testCage3.getAttributes().keys())

        self.assertTrue(type(self.testCage1.getAttributes()['strength'])==int)
        self.assertTrue(type(self.testCage1.getAttributes()['magic'])==int)
        self.assertTrue(type(self.testCage1.getAttributes()['play'])==int)
        self.assertTrue(type(self.testCage1.getAttributes()['supplies_vegetables'])==bool)
        self.assertTrue(type(self.testCage1.getAttributes()['supplies_meat'])==bool)
        self.assertTrue(type(self.testCage1.getAttributes()['removes_poo'])==bool)
        self.assertTrue(type(self.testCage1.getAttributes()['poo'])==int)

        self.assertTrue(type(self.testCage2.getAttributes()['strength'])==int)
        self.assertTrue(type(self.testCage2.getAttributes()['magic'])==int)
        self.assertTrue(type(self.testCage2.getAttributes()['play'])==int)
        self.assertTrue(type(self.testCage2.getAttributes()['supplies_vegetables'])==bool)
        self.assertTrue(type(self.testCage2.getAttributes()['supplies_meat'])==bool)
        self.assertTrue(type(self.testCage2.getAttributes()['removes_poo'])==bool)
        self.assertTrue(type(self.testCage2.getAttributes()['poo'])==int)

        self.assertTrue(type(self.testCage3.getAttributes()['strength'])==int)
        self.assertTrue(type(self.testCage3.getAttributes()['magic'])==int)
        self.assertTrue(type(self.testCage3.getAttributes()['play'])==int)
        self.assertTrue(type(self.testCage3.getAttributes()['supplies_vegetables'])==bool)
        self.assertTrue(type(self.testCage3.getAttributes()['supplies_meat'])==bool)
        self.assertTrue(type(self.testCage3.getAttributes()['removes_poo'])==bool)
        self.assertTrue(type(self.testCage3.getAttributes()['poo'])==int)

    def testPooingAndCleaning(self):
        self.assertEqual(self.testCage1.getAttributes()['poo'],0)
        self.assertTrue(self.testCage1.addPoo())
        self.assertTrue(self.testCage1.addPoo(2))
        self.assertEqual(self.testCage1.getAttributes()['poo'], 3)
        self.assertTrue(self.testCage1.cleanPoo())
        self.assertFalse(self.testCage1.cleanPoo(3))
        self.assertEqual(self.testCage1.getAttributes()['poo'],2)

    def testAddUpgrade(self):
        self.assertFalse(self.testCage1.expanded)
        oldstr=self.testCage1.getAttributes()['strength']
        self.assertTrue(self.testCage1.addUpgrade(self.testUpgrade1))
        self.assertEqual(self.testCage1.getAttributes()['strength'], , msg)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()