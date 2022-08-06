from kaprekar_6174 import *

def test_get_3_digit_non_repeating_num():
    return_num = get_4_digit_non_repeating_num()
    assert len(return_num) == 4
    assert ((return_num[0] != return_num[1]) & (return_num[0] != return_num[2]) & (return_num[0] != return_num[3]))

def test_sort_and_reverse():
    num, reversed_num = sort_and_reverse('8692')
    assert num == '9862'
    assert reversed_num == '2689'