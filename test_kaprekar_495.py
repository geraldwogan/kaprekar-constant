import unittest
# import main.kaprekar_495 as kap
from kaprekar_495 import * 

# class TestKaprekar495(unittest.TestCase):

#     def test_get_3_digit_non_repeating_num(self):
#         return_num = get_3_digit_non_repeating_num()
#         self.assertEqual(len(return_num), 3)

# unittest.main()

def test_get_3_digit_non_repeating_num():
    return_num = get_3_digit_non_repeating_num()
    assert len(return_num) == 3

