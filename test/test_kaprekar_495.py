# import the package
import main.kaprekar_495 as kap

def test_get_3_digit_non_repeating_num():
    return_num = kap.get_3_digit_non_repeating_num()
    assert len(return_num) == 3
