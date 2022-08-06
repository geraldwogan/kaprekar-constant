from kaprekar_495 import * 

def test_get_3_digit_non_repeating_num():
    return_num = get_3_digit_non_repeating_num()
    assert len(return_num) == 3
    assert (return_num[0] != return_num[1]) & (return_num[0] != return_num[2])

def test_sort_and_reverse():
    num, reversed_num = sort_and_reverse('869')
    assert num == '986'
    assert reversed_num == '689'

def test_get_nums_recurse():
    assert get_nums_recurse('954') == 495

def test_get_nums_recurse_2():
    assert get_nums_recurse('319') == 495