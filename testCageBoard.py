'''
Created on 7 feb. 2014

@author: Pieter
'''
import unittest
from dungeonz.CageBoard import CageBoard

class Test(unittest.TestCase):

    def setUp(self):
        self.cb1 = CageBoard(1)
        self.cb2 = CageBoard(2)
        self.cb3 = CageBoard(3)
        self.cb4 = CageBoard(4)

    def tearDown(self):
        del(self.cb1)
        del(self.cb2)
        del(self.cb3)
        del(self.cb4)

    def testConstructo(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()