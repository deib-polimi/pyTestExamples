#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:53:02 2020

@author: elisabettadinitto
"""

import unittest
import SimpleTest2
import SimpleTest

def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(SimpleTest2.SimpleTest2))
   suite.addTest(unittest.makeSuite(SimpleTest.SimpleTest))
   return suite
   
if __name__ == '__main__':
   runner = unittest.TextTestRunner()
   test_suite = suite()
   runner.run (test_suite)