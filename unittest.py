from class import *
import unittest

class TestCalculator(unittest.TestCase):
	def SetUp(self):
		pass
	def testadd(self):
		self.assertEqual(add(2,2),4,'ok')
		self.assertEqual(add(-3,2),-1,'ok')
		self.assertEqual(add(2,-1),1,'ok')
		self.assertEqual(add(-2,3),1,'ok')
	def testsub(self):
		self.assertEqual(sub(2,1),1,'ok')
		self.assertEqual(sub(1,2),-1,'ok')
		self.assertEqual(sub(-1,-2),1,'ok')
		self.assertEqual(sub(-1,2),-3,'ok')
	def testmul(self):
		self.assertEqual(mul(4,2),8,'ok')
		self.assertEqual(mul(4,-2),-8,'ok')
		self.assertEqual(mul(-2,-4),8,'ok')
		self.assertEqual(mul(-4,2),-8,'ok')
	def testdiv(self):
		self.assertEqual(div(4,2),2,'ok')
		self.assertEqual(div(-4,2),-2,'ok')
if __name__=='__main__":
unittest.main()