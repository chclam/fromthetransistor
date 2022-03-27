from gates import *
import unittest

class TestGates(unittest.TestCase):
  def test_nand(self):
    self.assertEqual(nand(0, 0), 1)
    self.assertEqual(nand(0, 1), 1)
    self.assertEqual(nand(1, 0), 1)
    self.assertEqual(nand(1, 1), 0)

  def test_not(self):
    self.assertEqual(not_(0), 1)
    self.assertEqual(not_(1), 0)
    
  def test_and(self):
    self.assertEqual(and_(0, 0), 0)
    self.assertEqual(and_(0, 1), 0)
    self.assertEqual(and_(1, 0), 0)
    self.assertEqual(and_(1, 1), 1)

  def test_or(self):
    self.assertEqual(or_(0, 0), 0)
    self.assertEqual(or_(0, 1), 1)
    self.assertEqual(or_(1, 0), 1)
    self.assertEqual(or_(1, 1), 1)

  def test_xor(self):
    self.assertEqual(xor(0, 0), 0)
    self.assertEqual(xor(0, 1), 1)
    self.assertEqual(xor(1, 0), 1)
    self.assertEqual(xor(1, 1), 0)

  def test_mux(self):
    self.assertEqual(mux(0, 0, 0), 0)
    self.assertEqual(mux(0, 1, 0), 0)
    self.assertEqual(mux(1, 0, 0), 1)
    self.assertEqual(mux(1, 1, 0), 1)
    self.assertEqual(mux(0, 0, 1), 0)
    self.assertEqual(mux(0, 1, 1), 1)
    self.assertEqual(mux(1, 0, 1), 0)
    self.assertEqual(mux(1, 1, 1), 1)

  def test_dmux(self):
    self.assertEqual(dmux(0, 0), (0, 0))
    self.assertEqual(dmux(1, 0), (1, 0))
    self.assertEqual(dmux(0, 1), (0, 0))
    self.assertEqual(dmux(1, 1), (0, 1))

  def test_multi_not(self):
    self.assertEqual(multi_not([0]), [1])
    self.assertEqual(multi_not([1]), [0])
    self.assertEqual(multi_not([0, 1]), [1, 0])

  def test_half_adder(self):
    self.assertEqual(half_adder(0, 0), (0, 0))
    self.assertEqual(half_adder(0, 1), (0, 1))
    self.assertEqual(half_adder(1, 0), (0, 1))
    self.assertEqual(half_adder(1, 1), (1, 0))

  def test_full_adder(self):
    self.assertEqual(full_adder(0, 0, 0), (0, 0))
    self.assertEqual(full_adder(0, 1, 0), (0, 1))
    self.assertEqual(full_adder(1, 0, 0), (0, 1))
    self.assertEqual(full_adder(1, 1, 0), (1, 0))
    self.assertEqual(full_adder(0, 0, 1), (0, 1))
    self.assertEqual(full_adder(0, 1, 1), (1, 0))
    self.assertEqual(full_adder(1, 0, 1), (1, 0))
    self.assertEqual(full_adder(1, 1, 1), (1, 1))
