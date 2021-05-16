#!/usr/bin/python3

import unittest
import math

def chop(i, i_array):
  return chop_inner(i, i_array, 0)

def chop_inner(i, i_array, inx):

  if len(i_array) == 0:
    return -1 
  elif len(i_array) == 1 and i_array[0] != i:
    return -1
  elif len(i_array) == 1 and i_array[0] == i:
    return inx

  size = math.floor(len(i_array)/2)

  left = i_array[:size]
  right = i_array[size:]

  if (len(right) > 0 and right[0] <= i):
    return chop_inner(i, right, inx + size)
  else:
    return chop_inner(i, left, inx)


class TestChop(unittest.TestCase):
  def tests(self):
    self.assertEqual(-1, chop(3, []))
    self.assertEqual(-1, chop(3, [1]))
    self.assertEqual(0,  chop(1, [1]))
    self.assertEqual(0,  chop(1, [1, 3, 5]))
    self.assertEqual(1,  chop(3, [1, 3, 5]))
    self.assertEqual(2,  chop(5, [1, 3, 5]))
    self.assertEqual(-1, chop(0, [1, 3, 5]))
    self.assertEqual(-1, chop(2, [1, 3, 5]))
    self.assertEqual(-1, chop(4, [1, 3, 5]))
    self.assertEqual(-1, chop(6, [1, 3, 5]))
    self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
    self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
    self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
    self.assertEqual(3,  chop(7, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
  unittest.main()
