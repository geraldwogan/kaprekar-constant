from random import randint

def get_3_digit_non_repeating_num():
    num = ''

    # # add rand int between 0-9 three times.
    for x in range(0,3):
        digit = str(randint(0,9))
        num += digit
    
    # repeated num check
    while num[0] == num[1] and num[1] == num[2]:
        print(f'error : {num}')
        num = get_3_digit_non_repeating_num()

    return num

def sort_and_reverse(num):
    # sorting nums
    num = ''.join(sorted(num, reverse=True))
    reverse_num = ''.join(sorted(num))

    return num, reverse_num

def get_nums_recurse(num):
    num, reverse_num = sort_and_reverse(num)

    print(num, '-', reverse_num)

    result = int(num) - int(reverse_num)

    if result == 495:
        print(f"success! {result} found.")
        return
    else:
        print(f"failure. result is {result}.")
        get_nums_recurse(str(result))

num = get_3_digit_non_repeating_num()

get_nums_recurse(num)