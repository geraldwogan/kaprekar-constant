from kaprekar_6174 import *

def test_get_3_digit_non_repeating_num():
    return_num = get_4_digit_non_repeating_num()
    assert len(return_num) == 4
    assert (return_num[0] != return_num[1]) & (return_num[0] != return_num[2]) & (return_num[0] != return_num[3])
