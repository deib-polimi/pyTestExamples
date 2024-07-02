# -*- coding: utf-8 -*-

import unittest
import simpleAdd
class SimpleTest(unittest.TestCase):
   def testadd1 (self):
      self.assertEqual(simpleAdd.add(4,5),9, 'your implementation is incorrect')
      self.assertEqual(simpleAdd.add(-4,-5),-9)
      self.assertEqual(simpleAdd.add(4,-5),-1)
      self.assertEqual(simpleAdd.add(-4,5),1)
      self.assertEqual(simpleAdd.add(0,0),0)
      self.assertEqual(simpleAdd.add(0,-5),-5)

   def testadd2 (self):
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
   