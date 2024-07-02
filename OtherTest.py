#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:52:35 2020

@author: elisabettadinitto
"""

import unittest
import simpleAdd
class OtherTest(unittest.TestCase):
   def testadd (self):
      self.assertTrue(simpleAdd.add(4,5) == 9, 'there is an error!')
      self.assertNotEqual(simpleAdd.add(-4,-5),9)
      input1 = [1, 2, -5, -10.999]
      input2 = [1, 2, -5, -10.999]
      resultSet = [2, 3, -4, -9.999, 4, -3, -8.999, -10, -15.999, -21.998]
      for a in input1 :
          for b in input2: 
              self.assertIn(simpleAdd.add(a, b), resultSet)

if __name__ == '__main__':
   unittest.main()