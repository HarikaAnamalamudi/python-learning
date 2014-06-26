
from classs import Calculator2 as Calc
import unittest

class TestCalculator (unittest.TestCase):
	def setUp(self):
		print ("STARTING TESTCASE")
		self.c = Calc()
		pass
	def tearDown(self):
		print ("ENDING TESTCASE")
		
	def testadd(self):
		self.assertEqual(self.c.add(2,2),4,'ok')
		self.assertEqual(self.c.add(-3,2),-1,'ok')
		self.assertEqual(self.c.add(2,-1),1,'ok')
		self.assertEqual(self.c.add(-2,3),1,'ok')
	
	def testsub(self):
		self.assertEqual(self.c.sub(2,1),1,'ok')
		self.assertEqual(self.c.sub(1,2),-1,'ok')
		self.assertEqual(self.c.sub(-1,-2),1,'ok')
		self.assertEqual(self.c.sub(-1,2),-3,'Failed comparison')
	
	def testmul(self):
		self.assertEqual(self.c.mul(4,2),8,'ok')
		self.assertEqual(self.c.mul(4,-2),-8,'ok')
		self.assertEqual(self.c.mul(-2,-4),8,'ok')
		self.assertEqual(self.c.mul(-4,2),-8,'ok')
	
	def testdiv(self):
		self.assertEqual(self.c.div(4,2),2,'ok')
		self.assertEqual(self.c.div(-4,2),-2,'ok')

if __name__== '__main__':
		unittest.main()
