from kaprekar_6174 import *

def test_get_3_digit_non_repeating_num():
    return_num = get_4_digit_non_repeating_num()
    assert len(return_num) == 4
    assert ((return_num[0] != return_num[1]) & (return_num[0] != return_num[2]) & (return_num[0] != return_num[3]))

def test_sort_and_reverse():
    num, reversed_num = sort_and_reverse('8692')
    assert num == '9862'
    assert reversed_num == '2689'

def test_get_nums_recurse():
    assert get_nums_recurse('8532') == 6174

def test_get_nums_recurse_2():
    assert get_nums_recurse('9862') == 6174