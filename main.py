from random import randint

def get_nums():
    # initialise num
    num = ''

    # add rand int between 0-9 three times.
    for x in range(0,3):
        digit = str(randint(0,9))
        num += digit
    
    # sorting nums
    num = ''.join(sorted(num, reverse=True))
    reverse_num = ''.join(sorted(num))
    
    # repeat num check
    if num[0] == num[1] and num[1] == num[2]:
        print('error : {num}')
        return '1234'

    return int(num), int(reverse_num)

def subtraction_recursion(num, reverse_num):
    result = num - reverse_num
    
    if result == 495:
        print(f"success! {result} found.")
    else:
        print(f"failure. result is {result}.")

num, reverse_num = get_nums()
print(num, reverse_num)
subtraction_recursion(num, reverse_num)
