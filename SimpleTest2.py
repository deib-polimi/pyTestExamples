#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:50:03 2019

@author: elisabettadinitto
"""

#this is file SimpleTest2
import unittest
import addSub
class SimpleTest2(unittest.TestCase):
    def setUp(self):
      name = self.shortDescription()
      if name == "Sub":
         self.a = 50
         self.b = 60
         print(name, self.a, self.b)
      if name == "Add":
         self.a = 10
         self.b = 20
         print(name, self.a, self.b, 'we are here')
    def tearDown(self):
      print('\nend of test',self.shortDescription())

    def testsub(self):
      """Sub"""
      self.assertEqual(addSub.sub(self.a, self.b), self.a-self.b, "This is a wrong implementation...")

    def testAdd(self):
      """Add"""
      self.assertEqual(addSub.add(self.a, self.b), self.a+self.b)
      
if __name__ == '__main__':
   unittest.main()
