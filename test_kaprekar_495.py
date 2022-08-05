from kaprekar_495 import * 

def test_get_3_digit_non_repeating_num():
    return_num = get_3_digit_non_repeating_num()
    assert len(return_num) == 3

def test_sort_and_reverse():
    num, reversed_num = sort_and_reverse('869')
    assert num == '986'
    assert reversed_num == '689'
