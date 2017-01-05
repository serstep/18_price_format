import unittest
from format_price import format_price

class TestPriceFormat(unittest.TestCase):

    def test_valid_full_float_part(self):
        formatted_price = format_price("37498234.49")
        self.assertIsNotNone(formatted_price)
        

    def test_invalid_without_float_part(self):
        formatted_price = format_price("65665")
        self.assertIsNone(formatted_price)
        

    def test_valid_zero_float_part(self):
        formatted_price = format_price("11.0")
        self.assertIsNotNone(formatted_price)
        

    def test_valid_zero_after_dot(self):
        formatted_price = format_price("7384934.07983")
        self.assertIsNotNone(formatted_price)
        

    def test_invalid_string_chars_in_int_part(self):
        formatted_price = format_price("ewde34.00")
        self.assertIsNone(formatted_price)
        

    def test_invalid_string_chars_in_float_part(self):
        formatted_price = format_price("34.00cdd")
        self.assertIsNone(formatted_price)
        

    def test_invalid_too_long_integer_part(self):
        formatted_price = format_price("234243423428943365964639534653734232334.00")
        self.assertIsNone(formatted_price)
        

    def test_invalid_too_long_float_part(self):
        formatted_price = format_price("9783634823.347985543965934675493657496579374650")
        self.assertIsNone(formatted_price)
        

    def test_invalid_many_dots(self):
        formatted_price = format_price("9783634823.34.798")
        self.assertIsNone(formatted_price)
    
    
    def test_invalid_negative(self):
        formatted_price = format_price("-34834.798")
        self.assertIsNone(formatted_price)
        

if __name__ == "__main__":

    unittest.main()
