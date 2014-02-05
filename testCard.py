'''
Created on 5 feb. 2014

@author: Pieter
'''
import unittest

from dungeonz.Card import Card

class Test(unittest.TestCase):

    def testConstructor(self):
        testCard1=Card("red","anger")
        self.assertFalse(testCard1.flipped)
        self.assertEqual(testCard1.numNeeds, 1)
        testCard2=Card("purple","dissease")
        self.assertFalse(testCard2.flipped)
        self.assertEqual(testCard2.numNeeds, 2)

    def testFlip(self):
        tC = Card("green","food")
        tC2 = Card("yellow","magic")
        self.assertFalse(tC.flipped)
        self.assertFalse(tC2.flipped)
        tC.turnCard()
        self.assertTrue(tC.flipped)
        tC.turnCard()
        self.assertFalse(tC.flipped)

    def testGetNeeds(self):
        tc1=Card("green","food")
        tc2=Card("red","food")
        self.assertEqual(type(tc1.getNeeds()), list)
        self.assertEqual(len(tc1.getNeeds()), 1)
        self.assertEqual(tc1.getNeeds(), ["food"])
        tc1.turnCard()
        self.assertEqual(type(tc1.getNeeds()), list)
        self.assertEqual(len(tc1.getNeeds()), 1)
        self.assertEqual(tc1.getNeeds(), ["food"])
        
        self.assertEqual(type(tc2.getNeeds()), list)
        self.assertEqual(len(tc2.getNeeds()), 1)
        self.assertEqual(tc2.getNeeds(), ["food"])
        tc2.turnCard()
        self.assertEqual(type(tc2.getNeeds()), list)
        self.assertEqual(len(tc2.getNeeds()), 2)
        self.assertEqual(tc2.getNeeds(), ["food","anger"])

        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConstructor']
    unittest.main()