'''
Created on 7 feb. 2014

@author: Pieter
'''
import unittest
from dungeonz.CageBoard import CageBoard
from dungeonz.Cage import Cage

class Test(unittest.TestCase):

    def setUp(self):
        self.cb1 = CageBoard(1)
        self.cb2 = CageBoard(2)
        self.cb3 = CageBoard(3)
        self.cb4 = CageBoard(4)
        self.tc1 = Cage("cage_1.png",strength=2,magic=1)
        self.tc2 = Cage("cage_6.png",magic=3)

    def tearDown(self):
        del(self.cb1)
        del(self.cb2)
        del(self.cb3)
        del(self.cb4)

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
        self.assertTrue(self.cb1.addCage(1, self.tc1))
        self.assertEqual(self.cb1.free, [False,True,True,True])
        self.assertEqual(self.cb1.cages[0], self.tc1)
        self.assertFalse(self.cb1.addCage(1, self.tc2))
        self.assertEqual(self.cb1.cages[0], self.tc1)

    Z
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()