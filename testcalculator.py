import unittest
from calculator import Calculator

class PythonExample(unittest,TestCase):
	def test_calculator_add_method(self):
		c=Calculator()
		result=c.add(2,2)
		self.assertEqual(4,result)
	def test_calculator_error_message_if_both_args_not_number(self):
		self.assertRaises(ValueError,self.c.add,'two','three')
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.add,'three',3)
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.add,3,'two')

	def test_calculator_sub_method(self):
		c=Calculator()
		result=c.sub(3,2)
		self.assertEqual(1,result)
	def test_calculator_error_message_if_both_args_not_number(self):
		self.assertRaises(ValueError,self.c.sub,'two','two')
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.sub,'three',3)
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.sub,3,'two')


	def test_calculator_mul_method(self):
		c=Calculator()
		result=c.mul(2,2)
		self.assertEqual(4,result)
	def test_calculator_error_message_if_both_args_not_number(self):
		self.assertRaises(ValueError,self.c.mul,'two','three')
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.mul,'three',3)
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.mul,3,'two')

	
	def test_calculator_div_method(self):
		c=Calculator()
		result=c.div(2,2)
		self.assertEqual(1,result)
	def test_calculator_error_message_if_both_args_not_number(self):
		self.assertRaises(ValueError,self.c.div,'two','three')
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.div,'three',3)
	def test_calculator_returns_error_message_if_x_arg_not_number(self):
		self.assertRaises(ValueError,self.c.div,3,'two')
if __name__=='__main__":
unittest.main()
        
	