#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:56:16 2020

@author: elisabettadinitto
"""

import unittest
import utilityFunctions
class UFTest(unittest.TestCase):
    def test1(self):
      self.assertEqual(utilityFunctions.listPalindromes('radar'), ['radar'])

    def test2(self):
        self.assertEqual(utilityFunctions.listPalindromes('adda'), ['adda'])
    
    def test3(self):
        self.assertEqual(utilityFunctions.listPalindromes('Adda'), ['Adda'])
    
    def test4(self):
        self.assertEqual(utilityFunctions.listPalindromes('radar adda'), ['radar', 'adda'])        
 
      
if __name__ == '__main__':
   unittest.main()